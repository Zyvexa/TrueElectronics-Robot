
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

#define SPEED 100


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
