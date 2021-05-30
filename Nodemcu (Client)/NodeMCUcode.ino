#include <Arduino.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <SPI.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Adafruit_Fingerprint.h>
ESP8266WiFiMulti WiFiMulti;

//####################################################

// bagian fingerprint
SoftwareSerial mySerial(D6, D5);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);
uint8_t id;
// bagian fingerprint

//####################################################


bool toogle_post = false;
bool toogle_post_access = false;
String data_finger = "none";
String data_finger1 = "none";
String data_finger2 = "none";
String data_finger3 = "none";
String data_finger4 = "none";
String data_finger5 = "none";
String data_finger6 = "none";
String data_finger7 = "none";
String data_finger8 = "none";
String data_finger9 = "none";
String data_finger10 = "none";
String data_finger11 = "none";
String data_finger12 = "none";
String data_finger13 = "none";
String data_finger14 = "none";
String data_finger15 = "none";
String data_finger16 = "none";
String data_finger17 = "none";
String data_finger18 = "none";
String data_finger19 = "none";
String data_finger20 = "none";
String data_finger_compare = "none";
String UID = "0";
int p;
bool toggle_akses = false;
void(*reset_all)(void) = 0;
const char* loker_address = "lockerapi";
String dataunlock;
int menuInput = 0;
int inputOTP = 0;



// global variabel

//####################################################
void setup() {
 //### batas setup###//
 
 Serial.begin(9600);
  
  // Serial.setDebugOutput(true);
  for (uint8_t t = 1; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP("Keluarga Lawak", "T4NY4APOTIK");
  
  // set the data rate for the sensor serial port
  finger.begin(57600);
 
 //### batas setup###//
}
//####################################################

//####################################################
void loop() {
  //### batas void loop ###//
  
  if ((WiFiMulti.run() == WL_CONNECTED)) {

    // perintah menjadalankan metode GET
    while (!toogle_post){
      String metode_get;
      metode_get = fungsi_http_get();
      Serial.println(metode_get);
      //unlock(dataunlock);
      delay(5000);
    }
    // perintah menjadalankan metode GET
  
    // perintah menjadalankan metode POST
    while (toogle_post){
      String metode_post;
      fungsi_http_post(UID , inputOTP , data_finger , data_finger1 , data_finger2);
      delay(5000);
    }
    // perintah menjadalankan metode POST

    // perintah menjadalankan metode POST AKSES
    while (toogle_post_access){
      String metode_post;
      fungsi_http_post(UID,0, data_finger_compare,"access",data_finger2);
      delay(5000);
    }
    // perintah menjadalankan metode POST AKSES
    
    
    }
    delay(10000);
    //### batas void loop ###//
}
//####################################################



//####################################################

// perintahi enroll
void perintah_enroll(int y){
  data_finger_compare = "";
  
  Serial.println("Melakukan proses scanning");
  id = 1;
  if (id == 0) {// ID #0 not allowed, try again!
    return;}
  getFingerprintEnroll(y);
}
// perintah enroll

//####################################################

int readnumber(void) {
  int num = 0;
  
  while (num == 0) {
    while (! Serial.available());
    num = Serial.parseInt();
  }
  return num;
}

//####################################################

// fungsi get
String fungsi_http_get(void){

WiFiClient client;
HTTPClient http;

    Serial.print("[HTTP] begin...\n");
    if (http.begin(client, "http://192.168.1.10:8090/getdlapi")) {  // HTTP
      Serial.print("[HTTP] GET...\n");
      // start connectio\n and send HTTP header
      int httpCode = http.GET();

      // httpCode will be negative on error
      if (httpCode > 0) {
        // HTTP header has been send and Server response header has been handled
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);

        // file found at server
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          // bagian json
          const size_t capacity = JSON_OBJECT_SIZE(2) + 20;
          DynamicJsonDocument doc(capacity);
          // bagian json
          String payload = http.getString();
          Serial.println(payload);
          // Parse JSON object
            DeserializationError error = deserializeJson(doc,payload);
            yield();
            if (error) {
              Serial.print(F("deserializeJson() failed: "));
              Serial.println(error.c_str());
              //return;
            } 
              // data locker
              int id_locker = doc["id"]; // 0
              int id_enroll = doc["id_enroll"]; // 0
              int toggle_verifikasi = doc["verifikasi"]; // 0

              if (toggle_verifikasi == 0 and id_enroll == 0 and id_locker == 0){
               perintah_enroll(21);
                  if (data_finger_compare != "none"){
                    //toogle_post_access = true;
                    
                    fungsi_http_post(UID,0, data_finger_compare,"access",data_finger2);
                    }}

      

              if (toggle_verifikasi == 1){
                Serial.print("Masukan OTP anda : ");
                inputOTP = readnumber();
                delay(1000);
                if (inputOTP != 0){
                  toogle_post = true;
                  UID = "0";
                  }
                }
           

             if (id_enroll != 0){
              Serial.println("enroll");
              for(int y = 0; y<=5;y++){
                if (y==0){
                  data_finger1 = "";
                  }
                perintah_enroll(y);
                
                delay(100);}
               if (data_finger1 != "none"){
                toogle_post = true;
                UID = id_enroll;
                }  
              }


                
                 if (id_locker == 1){
                  Serial.println("Locker 1 terbuka");
                  }
                  else if (id_locker == 2){
                  Serial.println("Locker 2 terbuka");
                  }
                  else if (id_locker == 3){
                  Serial.println("Locker 3 terbuka");
                  }
                  else if (id_locker == 4){
                  Serial.println("Locker 4 terbuka");
                  }
                  else if (id_locker == 5){
                  Serial.println("Locker 5 terbuka");
                  }
                  else if (id_locker == 6){
                  Serial.println("Locker 6 terbuka");
                  }
                  else if (id_locker == 7){
                  Serial.println("Locker 7 terbuka");
                  }
                  else if (id_locker == 8){
                  Serial.println("Locker 8 terbuka");
                  }
                  else if (id_locker == 9){
                  Serial.println("Locker 9 terbuka");
                  }
                  else if (id_locker == 10){
                  Serial.println("Locker 10 terbuka");
                  }
                  else{Serial.println("Semua Locker terkunci");}
                 
                

           // Parse JSON object
          //return payload;
        }
      } else {
        Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }

      http.end();
    } else {
      Serial.printf("[HTTP} Unable to connect\n");
    }
  
}
// fungsi get

//####################################################

// fungsi post
String fungsi_http_post(String user_id , int inputOTP , String d, String d1, String d2){

 WiFiClient client;
    HTTPClient http;

    Serial.print("[HTTP] begin...\n");
    String dataotp = String(inputOTP);
    // configure traged server and url
    if(d1 != "access"){
    http.begin(client, "http://192.168.1.10:8090/getduapi/"+user_id+"/"+dataotp+"/"+d1); }
    else if(user_id == "0" and inputOTP != 0 ){
      http.begin(client, "http://192.168.1.10:8090/getduapi/"+user_id+"/"+dataotp+"/"+d+"/"+d1+"/"+d2);
      }
    else if(d1 == "access" or d1 == "access_checkout"){
      http.begin(client, "http://192.168.1.10:8090/datafingercompare/"+d1+"/"+d);
      }
    http.addHeader("Content-Type", "text/plain");

    Serial.print("[HTTP] POST...\n");
    // start connection and send HTTP header and body
    int httpCode = http.POST("");

    // httpCode will be negative on error
    if (httpCode > 0) {
      // HTTP header has been send and Server response header has been handled
      Serial.printf("[HTTP] POST... code: %d\n", httpCode);

      // file found at server
      if (httpCode == HTTP_CODE_OK) {
        const String& payload = http.getString();
        

      }
    } else {
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
    // ubah kembali toggle_post menjadi false
        

    http.end();
 reset_all();
      
}
// fungsi post


//####################################################
// fungsi enroll

uint8_t getFingerprintEnroll(int y) {

  p = -1;
  Serial.print("Menunggu jari untuk discan");;
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      Serial.println("\nImage taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.print(",");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      break;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      break;
    default:
      Serial.println("Unknown error");
      break;
    }
  }

  // OK success!

  p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }
  
  Serial.print("Remove finger ");
  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER) {
    p = finger.getImage();
  }
 
  p = -1;
  Serial.println("Place same finger again");
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      Serial.println("\nImage taken");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.print(".");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      break;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("Imaging error");
      break;
    default:
      Serial.println("Unknown error");
      break;
    }
  }

  // OK success!

  p = finger.image2Tz(2);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.println("Image converted");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("Image too messy");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("Communication error");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("Could not find fingerprint features");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("Could not find fingerprint features");
      return p;
    default:
      Serial.println("Unknown error");
      return p;
  }
  
  // OK converted!
  Serial.print("Creating model for #");
  
  p = finger.createModel();
  if (p == FINGERPRINT_OK) {
    Serial.println("Prints matched!");
  p = 1;
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_ENROLLMISMATCH) {
    Serial.println("Fingerprints did not match");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }

    downloadFingerprintTemplate(id, y); 
}

// fungsi enroll

//####################################################

// fungsi get template

uint8_t downloadFingerprintTemplate(uint16_t id,int y)
{

  p;
      
  Serial.print("==> Attempting to get Templete #"); Serial.println(id);
  p = finger.getModel();
  switch (p) {
    case FINGERPRINT_OK:
      Serial.print("Template "); Serial.print(id); Serial.println(" transferring:");
      break;
   default:
      Serial.print("Unknown error "); Serial.println(p);
      return p;
  }

  uint8_t bytesReceived[900];

  int i = 0;
  while (i <= 554 ) { 
      if (mySerial.available()) {
          bytesReceived[i++] = mySerial.read();
      }
  }
  Serial.println("Decoding packet...");
  
  // Filtering The Packet
  int a = 0, x = 3;;
  
  for (int i = 10; i <= 554; ++i) {
      
        if (y == 1){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger1 += olahData;}
        
        else if (y == 2){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger1 += olahData;}

        else if (y == 3){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger1 += olahData;}

        else if (y == 4){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger1 += olahData;}

        else if (y == 5){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger1 += olahData;}

        else if (y == 6){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger6 += olahData;}
        
        else if (y == 7){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger7 += olahData;}

        else if (y == 8){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger8 += olahData;}

        else if (y == 9){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger9 += olahData;}

        else if (y == 10){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger10 += olahData;}

        else if (y == 11){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger11 += olahData;}
        
        else if (y == 12){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger12 += olahData;}

        else if (y == 13){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger13 += olahData;}

        else if (y == 14){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger14 += olahData;}

        else if (y == 15){
         String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger15 += olahData;}

        else if (y == 16){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger16 += olahData;}
        
        else if (y == 17){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger17 += olahData;}

        else if (y == 18){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger18 += olahData;}

        else if (y == 19){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger19 += olahData;}

        else if (y == 20){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger20 += olahData;}

        else if (y == 21){
        String olahData = printHex(bytesReceived[i-1] , 2);
        data_finger_compare += olahData;}
      }
  
}

String printHex(int num, int precision) {
    char tmp[16];
    char format[128];
 
    sprintf(format, "%%.%dX", precision);
 
    sprintf(tmp, format, num);
    //Serial.print(tmp);
    return tmp;
}

// fungsi get template

//####################################################
