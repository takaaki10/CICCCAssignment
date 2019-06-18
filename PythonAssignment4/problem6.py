'''
Implement a function which receives a 2D list which represent the following grid:

■　□　□　□　□　□　□　■　■　□
□　□　■　□　□　□　□　□　□　□
□　■　■　■　■　■　□　□　□　□
□　□　□　□　□　■　□　□　■　□
□　□　□　□　□　■　□　□　■　□
□　■　■　■　■　■　□　□　■　□
□　□　□　□　□　■　□　□　□　□
□　□　□　■　■　■　■　□　□　□

The dark cell means they are empty.

Each cell is associated a number (called weight) based on its row’s and column’s number.
The number is calculated using this formula: (i+j)*3-10. For instance the cell[4][5] = (4+5)*3-10=27-10=17
- The function should find the cell whose total sum of it’s neighbour weight is maximum and
return a tuple which contains the row and column of the cell.
The numbers of a cell is defined as all cells that have an edge in common with the cell.
For instance the　neighbours of the green cell is all the red cells:

■　□　□　□　□　□　□　■　■　□
□　□　■　□　□　□　□　□　□　□
□　■　■　■　■　■　▲　□　□　□
□　□　□　□　□　■　●　▲　■　□　　▲　Red
□　□　□　□　□　■　▲　□　■　□　　●　Green
□　■　■　■　■　■　□　□　■　□
□　□　□　□　□　■　□　□　□　□
□　□　□　■　■　■　■　□　□　□


以下のグリッドを表す2Dリストを受け取る関数を実装してください。

■　□　□　□　□　□　□　■　■　□
□　□　■　□　□　□　□　□　□　□
□　■　■　■　■　■　□　□　□　□
□　□　□　□　□　■　□　□　■　□
□　□　□　□　□　■　□　□　■　□
□　■　■　■　■　■　□　□　■　□
□　□　□　□　□　■　□　□　□　□
□　□　□　■　■　■　■　□　□　□

暗いセルは、それらが空であることを意味します。

各セルには、行と列の番号に基づいて番号（ウェイトと呼ばれる）が関連付けられています。
数はこの公式を使用して計算されます：（i + j）* 3-10。 たとえば、セル[4] [5] =（4 + 5）* 3-10 = 27-10 = 17
 - 関数は、隣接する重みの合計が最大になるセルを見つけ、そのセルの行と列を含むタプルを返します。
 セルの番号は、セルと共通のエッジを持つすべてのセルとして定義されます。 たとえば、緑色のセルの隣人はすべて赤のセルです。

■　□　□　□　□　□　□　■　■　□
□　□　■　□　□　□　□　□　□　□
□　■　■　■　■　■　▲　□　□　□
□　□　□　□　□　■　●　▲　■　□　　▲　Red
□　□　□　□　□　■　▲　□　■　□　　●　Green
□　■　■　■　■　■　□　□　■　□
□　□　□　□　□　■　□　□　□　□
□　□　□　■　■　■　■　□　□　□

'''



