from pyabsa import AspectPolarityClassification as APC
from pyabsa.tasks.AspectPolarityClassification import SentimentClassifier
from pyabsa import available_checkpoints
from pyabsa import DatasetItem

# find a suitable checkpoint and use the name:
sentiment_classifier = APC.SentimentClassifier(
    checkpoint="D:\\project\\PyABSA\\checkpoints\\fast_lsa_t_v2_AttractionReviewId_acc_80.8_f1_76.25",
)

sentiment_classifier.batch_predict(
    target_file=DatasetItem('attraction', '522.attraction_id_test'),  # the batch_predict() is only available for a file only, please put the examples in a file
    print_result=True,
    save_result=True,
    ignore_error=True,
    eval_batch_size=32,
)