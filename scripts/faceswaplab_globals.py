import os
from modules import scripts

MODELS_DIR = os.path.abspath(os.path.join("models", "faceswaplab"))
ANALYZER_DIR = os.path.abspath(os.path.join(MODELS_DIR, "analysers"))
FACE_PARSER_DIR = os.path.abspath(os.path.join(MODELS_DIR, "parser"))
FACES_DIR = os.path.abspath(os.path.join(MODELS_DIR, "faces"))

REFERENCE_PATH = os.path.join(
    scripts.basedir(), "extensions", "sd-webui-faceswaplab", "references"
)

VERSION_FLAG: str = "v1.2.1"
EXTENSION_PATH = os.path.join("extensions", "sd-webui-faceswaplab")

# The NSFW score threshold. If any part of the image has a score greater than this threshold, the image will be considered NSFW.
NSFW_SCORE_THRESHOLD: float = 0.7
EXPECTED_INSWAPPER_SHA1 = "17a64851eaefd55ea597ee41e5c18409754244c5"
