from mngscore_V2 import ScoreManager

# score_manager = ScoreManager()
# score_manager.run()

score_manager = ScoreManager("scores_test.json", ["국어", "영어", "수학", "과학", "사회"])
score_manager.run()