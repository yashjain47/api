
'For Manual Addition of File Name'
# __all__=["product_controller","user_controller",]



'For Automatic Addition of File Name'
import os, glob
__all__=[os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]