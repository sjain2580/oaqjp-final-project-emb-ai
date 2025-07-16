import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]
        for text, expected_emotion in test_cases:
            with self.subTest(text=text): # This allows individual failures to be reported clearly
                result = emotion_detector(text)
                
                # Print the result for each emotion as requested
                print(f"Text: '{text}' -> Result: {result}")

                # Check if the API call was successful and returned a dominant emotion
                self.assertIsNotNone(result.get('dominant_emotion'), 
                                     f"Dominant emotion not found for '{text}'")
                
                # Assert that the detected dominant emotion matches the expected emotion
                self.assertEqual(result['dominant_emotion'], expected_emotion, 
                                 f"Expected '{expected_emotion}' for '{text}', but got '{result['dominant_emotion']}'")

if __name__ == '__main__':
    unittest.main()