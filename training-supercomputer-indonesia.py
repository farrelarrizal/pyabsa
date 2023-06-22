def baseline_scenario(pretrained):
    # Load checkpoint
    # checkpoint = ''

    # Load dataset
    dataset = DatasetItem("AttractionReviewId", "521.attraction_id")

    # Load config model
    config = APC.APCConfigManager.get_apc_config_english()
    config.num_epoch = 15
    config.learning_rate = 2e-05
    config.model = APCModelList.FAST_LSA_T_V2
    config.pretrained_bert = pretrained
    config.cache_dataset = False
    config.max_seq_len = 105
    config.lsa = True
    config.l2reg = 1e-05
    config.optimizer = 'adamw'
    config.eta_lr = 0.01
    config.batch_size = 16

    config.scenario_case = "baseline scenario"

    # Train model
    Notification.send('Training started!')
    try:
        trainer = APC.APCTrainer(
            config=config,
            dataset=dataset,
            # from_checkpoint=checkpoint,  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
            auto_device=DeviceTypeOption.CUDA,
            path_to_save=None,
            # set a path to save checkpoints, if it is None, save checkpoints at 'checkpoints' folder
            checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,
            load_aug=False,
            # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
        )

        Notification.send('Training completed!')
        print('result', trainer)
    except Exception as e:
        Notification.send(f'Training failed! {e}')
        raise e

def scenario_id_b_01():

    # Load checkpoint
    checkpoint = 'D:\\project\\PyABSA\\checkpoints\\ID_A_02_fast_lsa_t_v2_AttractionReviewId_acc_80.8_f1_76.25'

    # Load dataset
    dataset = DatasetItem("AttractionReviewId", "521.attraction_id")

    # Load config model
    config = APC.APCConfigManager.get_apc_config_english()
    config.learning_rate = 2e-5
    config.model = APCModelList.FAST_LSA_T_V2
    config.pretrained_bert = 'indobenchmark/indobert-large-p2'
    config.cache_dataset = False
    config.max_seq_len = 135
    # config.max_seq_len = 105
    config.num_epoch = 15
    config.batch_size = 16
    config.lsa = True
    config.scenario_case = 'SCENARIO ID-B-01 CONTINUES BASELINE SCENARIO'

    # Train model
    Notification.send(f'Training started! {config.pretrained_bert}')
    try:
        trainer = APC.APCTrainer(
            config=config,
            dataset=dataset,
            from_checkpoint=checkpoint,  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
            auto_device=DeviceTypeOption.CUDA,
            path_to_save=None,  # set a path to save checkpoints, if it is None, save checkpoints at 'checkpoints' folder
            checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,
            load_aug=False,  # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
        ).destroy()
        Notification.send('Training completed!')
    except Exception as e:
        Notification.send(f'Training failed! {e}')
        raise e


# batch size = 8
def scenario_id_b_02():

    # Load checkpoint
    # checkpoint = 'D:\\project\\PyABSA\\checkpoints\\fast_lsa_t_v2_AttractionReviewEn_acc_91.82_f1_86.05'

    # Load dataset
    dataset = DatasetItem("AttractionReviewId", "521.attraction_id")

    # Load config model
    config = APC.APCConfigManager.get_apc_config_english()
    config.learning_rate = 2e-5
    config.model = APCModelList.FAST_LSA_T_V2
    config.pretrained_bert = 'indobenchmark/indobert-large-p2'
    config.cache_dataset = False
    config.max_seq_len = 105
    config.num_epoch = 15
    config.batch_size = 8
    config.lsa = True
    config.scenario_case = 'SCENARIO ID-B-02 (BATCH SIZE 8)'

    # Train model
    Notification.send(f'Training started! {config.pretrained_bert}')
    try:
        trainer = APC.APCTrainer(
            config=config,
            dataset=dataset,
            # from_checkpoint=checkpoint,  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
            auto_device=DeviceTypeOption.CUDA,
            path_to_save=None,  # set a path to save checkpoints, if it is None, save checkpoints at 'checkpoints' folder
            checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,
            load_aug=False,  # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
        ).destroy()
        Notification.send('Training completed!')
    except Exception as e:
        Notification.send(f'Training failed! {e}')
        raise e


# batch size = 24
def scenario_id_b_03():

    # Load checkpoint
    # checkpoint = 'D:\\project\\PyABSA\\checkpoints\\fast_lsa_t_v2_AttractionReviewEn_acc_91.82_f1_86.05'

    # Load dataset
    dataset = DatasetItem("AttractionReviewId", "521.attraction_id")

    # Load config model
    config = APC.APCConfigManager.get_apc_config_english()
    config.learning_rate = 2e-5
    config.model = APCModelList.FAST_LSA_T_V2
    config.pretrained_bert = 'indobenchmark/indobert-large-p2'
    config.cache_dataset = False
    config.max_seq_len = 105
    config.num_epoch = 15
    config.batch_size = 24
    config.lsa = True
    config.scenario_case = 'SCENARIO EN-B-03 (BATCH SIZE 24)'

    # Train model
    Notification.send(f'Training started! {config.pretrained_bert}')
    try:
        trainer = APC.APCTrainer(
            config=config,
            dataset=dataset,
            # from_checkpoint=checkpoint,  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
            auto_device=DeviceTypeOption.CUDA,
            path_to_save=None,  # set a path to save checkpoints, if it is None, save checkpoints at 'checkpoints' folder
            checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,
            load_aug=False,  # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
        ).destroy()
        Notification.send('Training completed!')
    except Exception as e:
        Notification.send(f'Training failed! {e}')
        raise e


# batch size it depends on best scenario (b01 - b03) & applying dropout 0.3
def scenario_id_b_04(pretrained, batch_size):

    # Load checkpoint
    # checkpoint = 'D:\\project\\PyABSA\\checkpoints\\fast_lsa_t_v2_AttractionReviewEn_acc_91.82_f1_86.05'

    # Load dataset
    dataset = DatasetItem("AttractionReviewId", "521.attraction_id")

    # Load config model
    config = APC.APCConfigManager.get_apc_config_english()
    config.learning_rate = 2e-5
    config.model = APCModelList.FAST_LSA_T_V2
    config.pretrained_bert = pretrained
    config.cache_dataset = False
    config.max_seq_len = 105
    config.num_epoch = 15
    config.batch_size = batch_size
    config.lsa = True
    config.dropout = 0.3
    config.scenario_case = 'SCENARIO ID-B-04 (BATCH SIZE ... , DROP OUT 0.3)'

    # Train model
    Notification.send(f'Training started! {config.pretrained_bert}')
    try:
        trainer = APC.APCTrainer(
            config=config,
            dataset=dataset,
            # from_checkpoint=checkpoint,  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
            auto_device=DeviceTypeOption.CUDA,
            path_to_save=None,  # set a path to save checkpoints, if it is None, save checkpoints at 'checkpoints' folder
            checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,
            load_aug=False,  # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
        ).destroy()
        Notification.send('Training completed!')
    except Exception as e:
        Notification.send(f'Training failed! {e}')
        raise e


def scenario_id_b_05(dropout, batch_size):

    # Load checkpoint
    # checkpoint = 'D:\\project\\PyABSA\\checkpoints\\fast_lsa_t_v2_AttractionReviewEn_acc_91.82_f1_86.05'

    # Load dataset
    dataset = DatasetItem("AttractionReviewId", "521.attraction_id")

    # Load config model
    config = APC.APCConfigManager.get_apc_config_english()
    config.model = APCModelList.FAST_LSA_T_V2
    config.pretrained_bert = 'indobenchmark/indobert-large-p2'
    config.learning_rate = 1e-5
    config.l2reg = 1e-8
    config.eta = -1
    config.eta_lr = 1e-3
    config.cache_dataset = False
    config.max_seq_len = 105
    config.num_epoch = 15
    config.batch_size = batch_size
    config.lsa = True
    config.dropout = dropout
    config.scenario_case = f'SCENARIO EN-B-05 DROPOUT {dropout}'

    # Train model
    Notification.send(f'Training started! {config.pretrained_bert}')
    try:
        trainer = APC.APCTrainer(
            config=config,
            dataset=dataset,
            # from_checkpoint=checkpoint,  # if you want to resume training from our pretrained checkpoints, you can pass the checkpoint name here
            auto_device=DeviceTypeOption.CUDA,
            path_to_save=None,  # set a path to save checkpoints, if it is None, save checkpoints at 'checkpoints' folder
            checkpoint_save_mode=ModelSaveOption.SAVE_MODEL_STATE_DICT,
            load_aug=False,  # there are some augmentation dataset for integrated datasets, you use them by setting load_aug=True to improve performance
        ).destroy()
        Notification.send('Training completed!')
    except Exception as e:
        Notification.send(f'Training failed! {e}')
        raise e

if __name__ == '__main__':
    from utils import Notification
    import warnings
    warnings.filterwarnings('ignore')
    import discordwebhook

    # Importing for pyabsa
    from pyabsa import AspectPolarityClassification as APC
    from pyabsa.tasks.AspectPolarityClassification.models import APCModelList
    from pyabsa import ModelSaveOption, DeviceTypeOption
    from pyabsa import DatasetItem

    # pemilihan pretrained model
    # Notification.send('indobenchmark/indobert-base-p1 started!')
    # baseline_scenario('indobenchmark/indobert-base-p1')

    # Notification.send('indobenchmark/indobert-base-p2 started!')
    # baseline_scenario('indobenchmark/indobert-base-p2')
    #
    # Notification.send('indobenchmark/indobert-lite-large-p2 started!')
    # baseline_scenario('indobenchmark/indobert-lite-large-p2')  # dipilih karena memiliki akurasi yang lebih baik untuk dataset SmSA (review)

    # baseline_scenario('cahya/bert-base-indonesian-1.5G')

    # baseline_scenario('indobenchmark/indobert-large-p2')  # metrics paling tinggi dari indobenchmark
    # baseline_scenario('w11wo/indonesian-roberta-base-sentiment-classifier')
    # baseline_scenario('rizalmilyardi/IndobertTypeNews')
    # Notification.send('Running cahya/bert-base-indonesian-1.5G started!')
    # baseline_scenario('cahya/bert-base-indonesian-1.5G')
    # Notification.send('Running Scenario ID B 01')
    # scenario_id_b_01()
    #
    # Notification.send('Running Scenario ID B 02')
    # scenario_id_b_02()
    #
    # Notification.send('Running Scenario ID B 03')
    # scenario_id_b_03()
    #
    Notification.send('Running Scenario ID B 04')
    scenario_id_b_04('w11wo/indonesian-roberta-base-sentiment-classifier', 8)
    #
    # Notification.send('Running Scenario ID B 05')
    # scenario_id_b_04(16)
    #
    # Notification.send('Running Scenario ID B 6')
    # scenario_id_b_05(0.3, 8)
    #
    # Notification.send('Running Scenario ID B 7')
    # scenario_id_b_05(0.3, 16)
