import re
import string
import os
import os.path
import warnings
import numpy as np
from scipy.sparse import spmatrix, coo_matrix
from sklearn.base import BaseEstimator
from sklearn.linear_model.base import LinearClassifierMixin, SparseCoefMixin
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_files
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import pandas as pd
import syntok.segmenter as segmenter

try:
    import langdetect
    LANGDETECT=True
except:
    LANGDETECT=False
try:
    import cchardet as chardet
    CHARDET=True
except:
    CHARDET=False
try:
    import jieba
    JIEBA=True
except:
    JIEBA=False
