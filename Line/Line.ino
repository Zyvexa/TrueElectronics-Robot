#define BACK_LEFT_MOTOR 9  // motors
#define LEFT_MOTOR 6
#define BACK_RIGHT_MOTOR 10
#define RIGHT_MOTOR 5

#define RIGHT_SENSOR A0
#define LEFT_SENSOR A5
#define RIGHT_CENTRAL_SENSOR A1
#define LEFT_CENTRAL_SENSOR A4

#define SPEED 100

bool type_of_line = false; // true - black line, false - white line

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
  if(analogRead(RIGHT_CENTRAL_SENSOR) > analogRead(RIGHT_SENSOR)) type_of_line = true;
  else type_of_line = false;
}


void loop() {
  line(100, 0);
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


  max_color = max(max_color, left_central_sensor);
  max_color = max(max_color, right_central_sensor);
  max_color = max(max_color, left_sensor);
  max_color = max(max_color, right_sensor);

  min_color = min(min_color, left_central_sensor);
  min_color = min(min_color, right_central_sensor);
  min_color = min(min_color, left_sensor);
  min_color = min(min_color, right_sensor);

  int middle_color = min_color + (0.4 * (max_color - min_color));

  if ((left_central_sensor > middle_color and right_central_sensor > middle_color and !type_of_line) or (left_central_sensor < middle_color and right_central_sensor < middle_color and type_of_line)) {
    if (old_left_central_sensor > middle_color and old_right_central_sensor < middle_color) {
      if (type_of_line) {
        right_speed = max_speed;
        left_speed = min_speed;
      }
      else {
        right_speed = min_speed;
        left_speed = max_speed;
      }
    } else if (old_left_central_sensor < middle_color and old_right_central_sensor > middle_color) {
      if (type_of_line) {
        right_speed = min_speed;
        left_speed = max_speed;
      }
      else {
        right_speed = max_speed;
        left_speed = min_speed;
      }

    } else {
      ;
      // right_speed = max_speed;
      // left_speed = max_speed;
    }
  } else {
    if (type_of_line) {
      left_speed = map(right_central_sensor, min_color, max_color, min_speed, max_speed);
      right_speed = map(left_central_sensor, min_color, max_color, min_speed, max_speed);
    }
    else {
      left_speed = map(right_central_sensor, max_color, min_color, min_speed, max_speed);
      right_speed = map(left_central_sensor, max_color, min_color, min_speed, max_speed);
    }
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
