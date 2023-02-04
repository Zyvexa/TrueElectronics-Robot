enum MAP_point {
  P13,
  P14,
  P21,
  P22,
  P31,
  P32,
  P41,
  P42,
  P43,
  P51,
  P53,
  P61,
  P63,
  P64,
  P72,
  P74,
  M11,
  M12,
  M21,
  M22,
  M31,
  M32,
  M41,
  M42,
  M53,
  M54,
  M61,
  M62,
  M73,
  M74,
  M81,
  M82
};


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define BACK_LEFT_MOTOR 9  // motors
#define LEFT_MOTOR 6
#define BACK_RIGHT_MOTOR 10
#define RIGHT_MOTOR 5

#define RIGHT_SENSOR A0
#define LEFT_SENSOR A5
#define RIGHT_CENTRAL_SENSOR A1
#define LEFT_CENTRAL_SENSOR A4
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define INFINITE 1000000
#define MAX_NODES 100
int way[MAX_NODES] = {};
int Way_cost = 0;
byte my_position = P31;
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#define SPEED 100

struct Node {
  int cost;  // стоимость узла
};
// структура, описывающая ребро графа
struct Edge {
  int from, to;  // начальный и конечный узлы ребра
  int cost;      // стоимость ребра
};

void setup() {
  pinMode(BACK_LEFT_MOTOR, OUTPUT);
  pinMode(LEFT_MOTOR, OUTPUT);
  pinMode(BACK_RIGHT_MOTOR, OUTPUT);
  pinMode(RIGHT_MOTOR, OUTPUT);
  pinMode(RIGHT_SENSOR, INPUT);
  pinMode(LEFT_SENSOR, INPUT);
  pinMode(RIGHT_CENTRAL_SENSOR, INPUT);
  pinMode(LEFT_CENTRAL_SENSOR, INPUT);
  Serial.begin(9600);
}
enum Movement {
  to_crossroad,
  crossroad_straight,
  crossroad_turn_left,
  crossroad_turn_right,
  crossroad_L_turn_right,
  crossroad_L_turn_left
};


void loop() {
  ;
}



void map_worker() {
  for (int i = 0; way[i] != -1; i++) {
    Serial.print(way[i]);
    Serial.print(" ");
  }

  for (int i = 0; way[i] != -1; i++) {
    // Serial.println(way[i]);
    if (way[i] >= M11) {
      if (way[i] == M32) {
        if (my_position == P43) movement(crossroad_L_turn_right);
        else movement(crossroad_straight);

      } else if (way[i] == M41) {
        if (my_position == P41) movement(crossroad_straight);
        else movement(crossroad_turn_left);

      } else if (way[i] == M74) {
        if (my_position == P41) movement(crossroad_turn_left);
        else movement(crossroad_turn_right);

      } else if (way[i] == M53) {  ////////////////////////////////////////////////////////////////
        if (my_position == P61) movement(crossroad_turn_right);
        else movement(crossroad_straight);

      } else if (way[i] == M81) {
        if (my_position == P61) movement(crossroad_turn_left);
        else movement(crossroad_straight);

      } else if (way[i] == M62) {
        if (my_position == P63) movement(crossroad_turn_right);
        else movement(crossroad_turn_left);
      } else if (way[i] == M42 or way[i] == M61) {  //////////////////////////////////////////////////////////////
        movement(crossroad_turn_right);
      } else if (way[i] == M54 or way[i] == M73) {
        movement(crossroad_turn_left);
      } else {
        movement(crossroad_straight);
      }
    } else movement(to_crossroad);
    my_position = way[i];
  }
}

void way_from_to(int from, int to) {
  Way_cost = 0;
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
    Way_cost = Way_cost + nodes[way[i]].cost;
  }
}
void initGraph(Node nodes[], int numNodes, Edge edges[], int numEdges) {
  // инициализируем узлы
  for (int i = 0; i < numNodes; i++) nodes[i].cost = INFINITE;

  // инициализируем ребра
  for (int i = 0; i < numEdges; i++) {
    edges[i].from = 0;
    edges[i].to = 0;
    edges[i].cost = INFINITE;
  }
}

int invway[MAX_NODES] = {};
void dijkstra(Node nodes[], int numNodes, Edge edges[], int numEdges,
              int start, int end) {

  for (int i = 0; i < 100; i++) way[i] = -1;

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
    current = previous[current];
  }
  // distation_len = distance[end];
  d--;
  for (int g = 0; d >= 0; g++) {
    way[g] = invway[d];
    invway[d] = 0;
    d--;
  }
  return distance[end];
}

void movement(int directions) {
  switch (directions) {
    case to_crossroad:
      while (digitalRead(LEFT_SENSOR) == 0 or digitalRead(RIGHT_SENSOR) == 0) {
        line(SPEED, 0);
      }
      move_motor(0, 0);
      break;

    case crossroad_straight:
      while (digitalRead(LEFT_SENSOR) != 0 or digitalRead(RIGHT_SENSOR) != 0) {
        move_motor(SPEED, SPEED);
      }
      move_motor(0, 0);
      break;
    case crossroad_turn_left:
      while (digitalRead(LEFT_SENSOR) != 0 or digitalRead(RIGHT_SENSOR) != 0) {
        move_motor(SPEED, SPEED);
      }
      while (digitalRead(RIGHT_SENSOR) == 0) {
        move_motor(0, SPEED);
      }
      while (digitalRead(RIGHT_CENTRAL_SENSOR) == 0) {
        move_motor(0, SPEED);
      }
      move_motor(0, 0);
      break;
    case crossroad_turn_right:
      while (digitalRead(LEFT_SENSOR) != 0 or digitalRead(RIGHT_SENSOR) != 0) {
        move_motor(SPEED, SPEED);
      }
      while (digitalRead(LEFT_SENSOR) == 0) {
        move_motor(SPEED, 0);
      }
      while (digitalRead(LEFT_CENTRAL_SENSOR) == 0) {
        move_motor(SPEED, 0);
      }
      move_motor(0, 0);
      break;
    case crossroad_L_turn_right:
      while (digitalRead(LEFT_SENSOR) != 0 or digitalRead(RIGHT_SENSOR) != 0) {
        move_motor(SPEED, SPEED);
      }
      while (digitalRead(RIGHT_SENSOR) == 0) {
        move_motor(SPEED, 0);
      }
      while (digitalRead(LEFT_CENTRAL_SENSOR) == 0) {
        move_motor(SPEED, 0);
      }
      move_motor(0, 0);
      break;
    case crossroad_L_turn_left:
      while (digitalRead(LEFT_SENSOR) != 0 or digitalRead(RIGHT_SENSOR) != 0) {
        move_motor(SPEED, SPEED);
      }
      while (digitalRead(LEFT_SENSOR) == 0) {
        move_motor(0, SPEED);
      }
      while (digitalRead(RIGHT_CENTRAL_SENSOR) == 0) {
        move_motor(0, SPEED);
      }
      move_motor(0, 0);
      break;
  }
}
int max_color = 0;
int min_color = 1023;
int old_left_central_sensor = 0;
int old_right_central_sensor = 0;
int old_left_sensor = 0;
int old_right_sensor = 0;
void line(int max_speed, int min_speed) {
  int right_speed = 0;
  int left_speed = 0;
  int left_central_sensor = analogRead(LEFT_CENTRAL_SENSOR);
  int right_central_sensor = analogRead(RIGHT_CENTRAL_SENSOR);
  int left_sensor = analogRead(LEFT_SENSOR);
  int right_sensor = analogRead(RIGHT_SENSOR);


  if (left_central_sensor > max_color) max_color = left_central_sensor;
  if (right_central_sensor > max_color) max_color = right_central_sensor;
  if (left_sensor > max_color) max_color = left_sensor;
  if (right_sensor > max_color) max_color = right_sensor;

  if (right_sensor < min_color) min_color = right_sensor;
  if (left_sensor < min_color) min_color = left_sensor;
  if (right_central_sensor < min_color) min_color = right_central_sensor;
  if (left_central_sensor < min_color) min_color = left_central_sensor;

  int middle_color = min_color + (0.4 * (max_color - min_color));

  if (left_central_sensor < middle_color and right_central_sensor < middle_color) {
    if ((old_left_central_sensor > middle_color and old_right_central_sensor < middle_color) or (left_sensor > middle_color or old_left_sensor > middle_color)) {
      right_speed = max_speed;
      left_speed = min_speed;
    } else if ((old_left_central_sensor < middle_color and old_right_central_sensor > middle_color) or (right_sensor > middle_color or old_right_sensor > middle_color)) {
      right_speed = min_speed;
      left_speed = max_speed;
    } else {
      ;
      // right_speed = max_speed;
      // left_speed = max_speed;
    }
  } else {

    left_speed = map(right_central_sensor, min_color, max_color, min_speed, max_speed);
    right_speed = map(left_central_sensor, min_color, max_color, min_speed, max_speed);
    old_right_central_sensor = right_central_sensor;
    old_left_central_sensor = left_central_sensor;
    old_left_sensor = left_sensor;
    old_right_sensor = right_sensor;
  }
  move_motor(left_speed, right_speed);
}
void move_motor(int left_speed, int right_speed) {
  analogWrite(LEFT_MOTOR, left_speed);
  analogWrite(BACK_LEFT_MOTOR, left_speed);
  analogWrite(RIGHT_MOTOR, right_speed);
  analogWrite(BACK_RIGHT_MOTOR, right_speed);
}
