from utilities.db.db_manager import dbManager
from utilities.db.db_manager import dbManager

class workoutsModel:
	def __init__(self):
		pass


	def ViewMyWorkouts(self,userName):
		query = "SELECT Workout_type,workout_date,workout_time,trainingID FROM training WHERE  workout_date>= DATE(NOW()) AND user_host=%s"
		return dbManager.fetch(query, (userName,))

	def ViewWorkoutDetails(self,trainingID):
		query = "SELECT * FROM training WHERE trainingID=%s"
		return dbManager.fetch(query, (trainingID,))

	def ViewParticipant(self,trainingID):
		query = "SELECT * FROM participant as p inner join users as u on p.participant=u.User_name WHERE p.training=%s"
		return dbManager.fetch(query, (trainingID,))

	def ViewCallendar(self,userName):
		query = "SELECT * FROM participant as p inner join training as t on p.training=t.trainingID WHERE p.participant=%s"
		return dbManager.fetch(query, (userName,))

	def ViewFutureWorkout(self):
		query = "SELECT Workout_type,workout_date,workout_time,trainingID,location_lng,location_lat FROM training WHERE  workout_date>= DATE(NOW()) "
		return dbManager.fetch(query, ())

	def ViewFutureWorkout2(self):
		query = "SELECT Workout_type,trainingID,location_lng,location_lat FROM training WHERE  workout_date>= DATE(NOW()) "
		return dbManager.fetch(query, ())

	def list_Workouts_by_inputs(self, Workout_type, workout_date, workout_time, time_limit):
		query = "SELECT * FROM training WHERE Workout_type=%s AND workout_date = %s AND workout_time>=%s AND workout_time<=%s"
		return dbManager.fetch(query, (Workout_type, workout_date, workout_time, time_limit,))

	def insertWortkour(self,Workout_type,location_lat,location_lng,Gender,workout_date,workout_time,number_of_participants,user_host,desc,duration):
		query="INSERT INTO training (Workout_type,location_lat,location_lng,Gender,workout_date,workout_time,number_of_participants,user_host,description,duration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		return dbManager.commit(query, (Workout_type, location_lat, location_lng, Gender, workout_date, workout_time, number_of_participants, user_host,desc,duration))

	def lastInserted(self):
		query="SELECT * From training ORDER BY trainingID DESC LIMIT 1"
		return dbManager.fetch(query, ())

	#inbaraaa
	def show_type(self, trainingID):
		query = "SELECT Workout_type FROM training WHERE trainingID=%s"
		return dbManager.fetch(query, (trainingID,))

	def list_Workouts_by_inputs(self, Workout_type, workout_date, workout_time, time_limit):
		query = "SELECT * FROM training WHERE Workout_type=%s AND workout_date = %s AND workout_time>=%s AND workout_time<=%s"
		return dbManager.fetch(query, (Workout_type, workout_date, workout_time, time_limit,))








workoutsModel = workoutsModel()




