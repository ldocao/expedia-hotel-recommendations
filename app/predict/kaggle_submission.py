import pandas as pd



class KaggleSubmission(object):
    DATA_DIR = "../../../data/"
    OUTPUT = DATA_DIR + "kaggle_submission_prediction.csv"
    NUMBER_OF_ROWS = 2528243
    
    def __init__(self, appetence):
        self.appetence = appetence
        self.top_hotel = None

        
    def to_csv(self):
        self.top_hotel = self.find_most_appetent_hotel()
        self._check_prediction()
        self.top_hotel.to_csv(self.OUTPUT, index=False)

        
    def find_most_appetent_hotel(self, top=5):
        top_hotel_per_user = self.appetence.sort_values(by=["user_id","appetence"],
                                                        ascending=False).groupby("user_id").head(top)
        list_top_hotel = top_hotel_per_user.groupby("user_id")["hotel_cluster"].apply(lambda x: x.tolist())
        prediction_as_list = list_top_hotel.apply(lambda row: " ".join([str(x) for x in row]))
        prediction_as_list = prediction_as_list.reset_index()
        prediction_as_list.columns = ["id", "hotel_cluster"]
        return prediction_as_list


    def _check_prediction(self):
        self._check_unique_id()
        self._check_user_id()

        
    def _check_unique_id(self):
        if len(self.top_hotel) != self.NUMBER_OF_ROWS:
            raise IndexError("Number of rows must be {}".format(self.NUMBER_OF_ROWS))


    def _check_user_id(self):
        user_id = self.top_hotel["user_id"]
        number_of_unique_user_id = len(user_id.unique())
        number_of_user_id = len(user_id)
        if number_of_user_id != number_of_unique_user_id:
            raise IndexError("user_id are not unique")

        
    def __repr__(self):
        if self.top_hotel is None:
            return self.find_most_appetent_hotel()
        else:
            return self.top_hotel
