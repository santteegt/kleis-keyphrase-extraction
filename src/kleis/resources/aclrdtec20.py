"""resouces/aclrdtec20

Class ACL-RD-TEC-2.0.

"""
from kleis.config.config import ACLRDTEC20, FORMAT_ACLXML
from kleis.resources.corpus import Corpus
import kleis.resources.dataset as kl

class AclRdTec20(Corpus):
    """Class for ACL-RD-TEC-2.0 corpus"""
    def __init__(self):
        self._name = ACLRDTEC20
        self._lang = "en"
        super().__init__()

    def load_train(self):
        """Set train dataset"""
        dataset = dict(kl.load_dataset_raw(self._config['train-labeled'],
                                           [".xml"],
                                           suffix="xml",
                                           encoding=self._encoding))
        kl.preprocess_dataset(dataset,
                              lang=self._lang,
                              dataset_format=FORMAT_ACLXML)
        self._train = dataset

    def load_dev(self):
        """Set dev dataset"""
        dataset = dict(kl.load_dataset_raw(self._config['dev-labeled'],
                                           [".txt", ".ann", ".xml"],
                                           suffix="txt",
                                           encoding=self._encoding))
        kl.preprocess_dataset(dataset, lang=self._lang)
        self._dev = dataset

    def load_test(self):
        """Set test dataset"""
        dataset = dict(kl.load_dataset_raw(self._config['test-labeled'],
                                           [".txt", ".ann"],
                                           suffix="txt",
                                           encoding=self._encoding))
        dataset_part = kl.load_dataset_raw(self._config['test-unlabeled'],
                                           [".xml"],
                                           suffix="txt",
                                           encoding=self._encoding)
        for key, value in dataset_part:
            dataset[key]["raw"]["xml"] = value["raw"]["xml"]
        kl.preprocess_dataset(dataset, lang=self._lang)
        self._test = dataset
