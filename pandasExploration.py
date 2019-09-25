import pandas as pd
import numpy as np

df2 = pd.DataFrame([('parrot',   24.0, 'second'),
                    ('lion',     80.5, 1), 
                    ('monkey', np.nan, None)],
                    columns=('name', 'max_speed', 'rank'))
import pdb; pdb.set_trace()
x = df2.values