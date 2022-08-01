from utilities.db.db_manager import dbManager

class participantsModel:
    def __init__(self):
        pass

    def insertParticipant(self, trainingID, participantID):
        query = "INSERT INTO participant (participant,training) VALUES (%s, %s)"
        return dbManager.commit(query, (participantID,trainingID))

    def check_if_Im_at_list(self, participant, training):
        query = "SELECT * FROM participant WHERE participant=%s and training=%s"
        return dbManager.fetch(query, (participant, training,))

    def JoinWorkout(self, participant, training):
        query = "INSERT INTO participant(participant, training) VALUES(%s, %s)"
        return dbManager.commit(query, (participant, training,))

    def check_creator(self, trainingID, participant):
        query = "SELECT * FROM participant as p inner join training as t on p.training=t.trainingID WHERE t.trainingID=%s and t.user_host=%s"
        return dbManager.fetch(query, (trainingID, participant,))

    def deleteMySelfFromWorkout(self, participant, training):
        query = "DELETE FROM participant WHERE participant=%s and training =%s"
        return dbManager.commit(query, (participant, training,))

    def count_num_of_pariticipants(self, training):
        query = "SELECT  COUNT(*) AS countP FROM participant WHERE training=%s GROUP BY training"
        return dbManager.fetch(query, (training,))

    def check_num_of_participants_in_training(self, training):
        query = "SELECT * FROM training WHERE trainingID=%s"
        return dbManager.fetch(query, (training,))


participantsModel= participantsModel()