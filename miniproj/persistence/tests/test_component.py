import unittest
from core.classes import Order, Person, Drinks



class TestApp(unittest.TestCase):
    def test_when_existing_person_submits_request_to_round_it_adds_preference(self):
        # Arrange
        round = Order(1, "John Doe")
        requester = Person("Sally", "Smith", 12)
        brewRequest = brewRequest(requester)
        expected = ["Capuccino"]
        # Act
        round.submit_request(brewRequest)
        # Assert
        requests = round.get_requests()
        self.assertEqual(requests, expected)
        
#     def test_when_application_is_closed_app_data_is_saved_to_database(self):
#         # Arrange
#         db = Database()
#         dbMock = MagicMock(wraps=db)
#         app = app.App(db)
#         # Act
#         app.exit()
#         # Assert
#         dbMock.saveDrinks.assert_called()
#         dbMock.savePeople.assert_called()
#         dbMock.saveRounds.assert_called()