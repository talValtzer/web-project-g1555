from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.models.workoutsModel import workoutsModel
from utilities.models.participantsModel import participantsModel
from utilities.models.userModel import userModel
# main_menu blueprint definition
workoutDetails = Blueprint('workoutDetails',__name__, static_folder='static', static_url_path='/workoutDetails', template_folder='templates')

@workoutDetails.route('/workoutDetails')
def index():
    userName = session["user"]
    training = session['workoutID']

    workout = list(workoutsModel.ViewWorkoutDetails(session['workoutID']))
    participants = list(workoutsModel.ViewParticipant(session['workoutID']))
    trainID_row = workoutsModel.ViewWorkoutDetails(training)  #workout details
    print(workout)

    userInList = participantsModel.check_if_Im_at_list(session["user"], session['workoutID'])
    print(userInList)

    print("kkk")
    creator_row = participantsModel.check_creator(session['workoutID'], session["user"])
    print(creator_row)

    num_of_participants_now_row = participantsModel.count_num_of_pariticipants(training)
    print(num_of_participants_now_row)
    print("qqq")
    numOfParticipantsNow = num_of_participants_now_row[0][0]
    print(numOfParticipantsNow)

    train_limit_participant_row = participantsModel.check_num_of_participants_in_training(training)
    train_limit_participant_answer = train_limit_participant_row[0][7]
    print(train_limit_participant_answer)

    train_gender = trainID_row[0][4]
    print(train_gender)
    user_row = userModel.ViewUserDetails(userName)

    user_gender = user_row[0][6]
    print(user_gender)

    if train_gender != user_gender and train_gender != "Mixed" :
        gender_massage= "Sorry, you can't join, this workout for "
        return render_template('workoutDetails.html', workout=workout[0], current_user=userName,
                           participants=participants, gender_massage=gender_massage)

    if len(creator_row) < 1 and len(userInList) < 1 and numOfParticipantsNow < train_limit_participant_answer: #if the user is not the user host and he is not registered
        answer_creator = True
        print("yyyyyyyyyyyyyyyyyyyyy")
        return render_template('workoutDetails.html', workout=workout[0], current_user=userName,
                               participants=participants, answer_creator=answer_creator)

    if len(creator_row) < 1 and len(userInList) == 1: #if the user is not the user host and he is registered
        Im_at_list = True
        print("ffffffffffff")
        return render_template('workoutDetails.html', workout=workout[0], current_user=userName,
                               participants=participants, Im_at_list=Im_at_list)
    else:
        if numOfParticipantsNow == train_limit_participant_answer:
            participants_massage = "Sorry, this workout if full, you can't join"
            print("yyyyyyyuuuuuuuuuuuuuuuuyyyy")
            return render_template('workoutDetails.html', workout=workout[0], current_user=userName,
                                   participants=participants, participants_massage=participants_massage)
        else:
            answer = False
            return render_template('workoutDetails.html', workout=workout[0], current_user=userName,
                                   participants=participants, ppp=answer)




#---------inbar
@workoutDetails.route("/join_workout", methods=["GET"])
def joinWorkout():
    userName = session["user"]
    print(userName)
    training = session['workoutID']
    print(training)
    participantsModel.JoinWorkout(userName, training)
    #return render_template('workoutDetails.html')
    return redirect(url_for('workoutDetails.index'))

@workoutDetails.route("/delete_Myself", methods=["GET"])
def deleteMyself():
    userName = session["user"]
    userModel.LoginCheckExist(userName)
    training = session['workoutID']
    participantsModel.deleteMySelfFromWorkout(userName, training)
    return redirect(url_for('workoutDetails.index'))