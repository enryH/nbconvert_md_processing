# Notebook

Exported using 
```
jupyter nbconvert --to markdown simple_notebook.ipynb
```

![Placeholder PNG](out1.png)


```python
import pandas as pd
import numpy as np
np.random.seed(42)
data = np.random.random(size=(10,5))
pd.DataFrame(data)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.374540</td>
      <td>0.950714</td>
      <td>0.731994</td>
      <td>0.598658</td>
      <td>0.156019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.155995</td>
      <td>0.058084</td>
      <td>0.866176</td>
      <td>0.601115</td>
      <td>0.708073</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.020584</td>
      <td>0.969910</td>
      <td>0.832443</td>
      <td>0.212339</td>
      <td>0.181825</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.183405</td>
      <td>0.304242</td>
      <td>0.524756</td>
      <td>0.431945</td>
      <td>0.291229</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.611853</td>
      <td>0.139494</td>
      <td>0.292145</td>
      <td>0.366362</td>
      <td>0.456070</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.785176</td>
      <td>0.199674</td>
      <td>0.514234</td>
      <td>0.592415</td>
      <td>0.046450</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.607545</td>
      <td>0.170524</td>
      <td>0.065052</td>
      <td>0.948886</td>
      <td>0.965632</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.808397</td>
      <td>0.304614</td>
      <td>0.097672</td>
      <td>0.684233</td>
      <td>0.440152</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.122038</td>
      <td>0.495177</td>
      <td>0.034389</td>
      <td>0.909320</td>
      <td>0.258780</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.662522</td>
      <td>0.311711</td>
      <td>0.520068</td>
      <td>0.546710</td>
      <td>0.184854</td>
    </tr>
  </tbody>
</table>
</div>



## Another image
![Placeholder PNG](out2.png)


```python
print("done")
```

    done
    
