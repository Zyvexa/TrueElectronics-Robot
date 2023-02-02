#define INFINITE 1000000
#define MAX_NODES 100


struct Node {
  int cost;  // стоимость узла
};
// структура, описывающая ребро графа
struct Edge {
  int from, to;  // начальный и конечный узлы ребра
  int cost;      // стоимость ребра
};
enum MAP_point {
  P13,  //0
  P14,  ///1
  P21,  //2
  P22,  //3
  P31,  //4
  P32,  //5
  P41,  //6
  P42,  //7
  P43,  //8
  P51,  //9
  P53,  //10
  P61,  //11
  P63,  //12
  P64,  ///13
  P72,  //14
  P74,  //15
  M11,  //16
  M12,  //17
  M21,  //18
  M22,  //19
  M31,  //20
  M32,  //21
  M41,  //22
  M42,  //23
  M53,  //24
  M54,  //25
  M61,  //26
  M62,  //27
  M73,  //28
  M74,  //29
  M81,  //30
  M82   //31
};
int way[MAX_NODES] = {};
int f = 0;
void setup() {
  Serial.begin(9600);
  delay(1000);
  way_from_to(P51, P32,0);
  
  for (int i = 0; i < 100; i++) {
    Serial.print(way[i]);
    Serial.print(" ");
    
  }
  Serial.println();
  Serial.println(f);
}


int invway[MAX_NODES] = {};
// функция нахождения кратчайшего пути между двумя узлами графа
// используя алгоритм Дейкстры

void dijkstra(Node nodes[], int numNodes, Edge edges[], int numEdges,
              int start, int end) {

  for (int i = 0; i < 100; i++) {
    way[i] = -1;
  }
  int distance[MAX_NODES];
  int previous[MAX_NODES];
  for (int i = 0; i < numNodes; i++) distance[i] = INFINITE;
  distance[start] = 0;
  for (int i = 0; i < numNodes; i++) previous[i] = -1;

  bool unvisited[MAX_NODES];
  for (int i = 0; i < numNodes; i++) unvisited[i] = true;

  while (true) {
    int minNode = -1;
    int minDistance = INFINITE;
    for (int i = 0; i < numNodes; i++) {
      if (unvisited[i] && distance[i] < minDistance) {
        minNode = i;
        minDistance = distance[i];
      }
    }

    if (minNode == -1) break;

    unvisited[minNode] = false;

    for (int i = 0; i < numEdges; i++) {
      if (edges[i].from == minNode) {
        int to = edges[i].to;
        int cost = edges[i].cost;
        if (distance[to] > distance[minNode] + cost) {
          distance[to] = distance[minNode] + cost;
          previous[to] = minNode;

          for (int i = 0; i < 100; i++) {
          }
        }
      }
    }
  }
  // выводим путь
  int current = end;
  int d = 0;
  while (current != -1) {
    invway[d] = current;
    d++;
    // Serial.print(current);
    // Serial.print(" ");
    current = previous[current];
  }
  // Serial.println();

  d--;
  for (int g = 0; d >= 0; g++) {
    way[g] = invway[d];
    invway[d] = 0;
    // Serial.println(way[g]);
    d--;
  }
}
// P41 M41 P51 M54 P64 M81 P13 M11 P21
// 1   0    1  1    1   12  1   1  1   = 19


void loop() {
}



// структура, описывающая узел графа

// функция инициализации графа
void initGraph(Node nodes[], int numNodes, Edge edges[], int numEdges) {
  // инициализируем узлы
  for (int i = 0; i < numNodes; i++) {

    nodes[i].cost = INFINITE;
  }

  // инициализируем ребра
  for (int i = 0; i < numEdges; i++) {
    edges[i].from = 0;
    edges[i].to = 0;
    edges[i].cost = INFINITE;
  }
}

void way_from_to(int from, int to,int dist) {
  Node nodes[MAX_NODES];
  Edge edges[MAX_NODES];

  int numNodes = 32;
  int numEdges = 38;

  initGraph(nodes, numNodes, edges, numEdges);

  nodes[P13].cost = 1;
  nodes[P14].cost = 1;
  nodes[P21].cost = 1;
  nodes[P22].cost = 1;
  nodes[P31].cost = 1;
  nodes[P32].cost = 1;
  nodes[P41].cost = 1;
  nodes[P42].cost = 1;
  nodes[P43].cost = 1;
  nodes[P51].cost = 1;
  nodes[P53].cost = 1;
  nodes[P61].cost = 1;
  nodes[P63].cost = 1;
  nodes[P64].cost = 1;
  nodes[P72].cost = 1;
  nodes[P74].cost = 1;
  nodes[M11].cost = 1;
  nodes[M12].cost = 1;
  nodes[M21].cost = 1;
  nodes[M22].cost = 1;
  nodes[M31].cost = 2;
  nodes[M32].cost = 2;
  nodes[M41].cost = 0;
  nodes[M42].cost = 0;
  nodes[M53].cost = 1;
  nodes[M54].cost = 1;
  nodes[M61].cost = 0;
  nodes[M62].cost = 0;
  nodes[M73].cost = 1;
  nodes[M74].cost = 1;
  nodes[M81].cost = 12;
  nodes[M82].cost = 12;


  edges[0].from = M11;
  edges[0].to = P21;
  edges[0].cost = 0;
  edges[1].from = M21;
  edges[1].to = P31;
  edges[1].cost = 0;
  edges[2].from = M31;
  edges[2].to = P41;
  edges[2].cost = 0;
  edges[3].from = M41;
  edges[3].to = P51;
  edges[3].cost = 0;
  edges[4].from = M61;
  edges[4].to = P61;
  edges[4].cost = 0;
  edges[5].from = M81;
  edges[5].to = P13;
  edges[5].cost = 0;
  edges[6].from = M12;
  edges[6].to = P14;
  edges[6].cost = 0;
  edges[7].from = M22;
  edges[7].to = P22;
  edges[7].cost = 0;
  edges[8].from = M32;
  edges[8].to = P32;
  edges[8].cost = 0;
  edges[9].from = M42;
  edges[9].to = P42;
  edges[9].cost = 0;
  edges[10].from = M62;
  edges[10].to = P72;
  edges[10].cost = 0;
  edges[11].from = M82;
  edges[11].to = P63;
  edges[11].cost = 0;
  edges[12].from = M53;
  edges[12].to = P53;
  edges[12].cost = 0;
  edges[13].from = M73;
  edges[13].to = P43;
  edges[13].cost = 0;
  edges[14].from = M54;
  edges[14].to = P64;
  edges[14].cost = 0;
  edges[15].from = M74;
  edges[15].to = P74;
  edges[15].cost = 0;
  edges[16].from = P14;
  edges[16].to = M82;
  edges[16].cost = 0;
  edges[17].from = P13;
  edges[17].to = M11;
  edges[17].cost = 0;
  edges[18].from = P21;
  edges[18].to = M21;
  edges[18].cost = 0;
  edges[19].from = P22;
  edges[19].to = M12;
  edges[19].cost = 0;
  edges[20].from = P31;
  edges[20].to = M31;
  edges[20].cost = 0;
  edges[21].from = P32;
  edges[21].to = M22;
  edges[21].cost = 0;
  edges[22].from = P41;
  edges[22].to = M41;
  edges[22].cost = 0;
  edges[23].from = P41;
  edges[23].to = M74;
  edges[23].cost = 0;
  edges[24].from = P42;
  edges[24].to = M32;
  edges[24].cost = 0;
  edges[25].from = P42;
  edges[25].to = M74;
  edges[25].cost = 0;
  edges[26].from = P43;
  edges[26].to = M41;
  edges[26].cost = 0;
  edges[27].from = P43;
  edges[27].to = M32;
  edges[27].cost = 0;
  edges[28].from = P51;
  edges[28].to = M54;
  edges[28].cost = 0;
  edges[29].from = P53;
  edges[29].to = M42;
  edges[29].cost = 0;
  edges[30].from = P61;
  edges[30].to = M53;
  edges[30].cost = 0;
  edges[31].from = P61;
  edges[31].to = M81;
  edges[31].cost = 0;
  edges[32].from = P63;
  edges[32].to = M53;
  edges[32].cost = 0;
  edges[33].from = P63;
  edges[33].to = M62;
  edges[33].cost = 0;
  edges[34].from = P64;
  edges[34].to = M62;
  edges[34].cost = 0;
  edges[35].from = P64;
  edges[35].to = M81;
  edges[35].cost = 0;
  edges[36].from = P72;
  edges[36].to = M73;
  edges[36].cost = 0;
  edges[37].from = P74;
  edges[37].to = M61;
  edges[37].cost = 0;


  int start = from;
  int end = to;
  
  
  dijkstra(nodes, numNodes, edges, numEdges, start, end);

  for (int i = 0; way[i] != -1; i++) {
    Serial.print(nodes[way[i]].cost);
    Serial.print(" ");
    f = f + nodes[way[i]].cost;
  }
  Serial.println();
  
}