import "dart:io";
import "dart:math";

void main() {
  String name = stdin.readLineSync()!;
  if (name.length > 100) {
    print("Name is too long");
    return;
  }
  print(name);
}
