// Online calculators
// https://planetcalc.com/8110/
// https://www.allmath.com/slope-intercept-form.php
// https://www.wolframalpha.com/widgets/gallery/view.jsp?id=f93da8718e9af4861e32fab00dccec5f

// Did not finish, it does not calculate correctly for now :)

enum BallStatus {
  onLeft,
  overLine,
  onRight;
}

class Point {
  const Point({required this.x, required this.y});

  factory Point.origin() {
    return const Point(x: 0, y: 0);
  }

  final double x;
  final double y;

  void display() {
    print('Point($x, $y)');
  }
}

class Line {
  const Line({required this.x, required this.y, required this.c});

  final double x;
  final double y;
  final double c;

  void display() {
    print('y = (${x}x) + ($c)');
  }
}

class Calculator {
  double getSlopeOf2Points(Point point1, Point point2) {
    final X1 = point1.x;
    final Y1 = point1.y;
    final X2 = point2.x;
    final Y2 = point2.y;

    final M = (Y2 - Y1) / (X2 - X1);

    return M;
  }

  Line getLineOf2Points(Point point1, Point point2) {
    final X1 = point1.x;
    final Y1 = point1.y;
    final X2 = point2.x;

    final M = getSlopeOf2Points(point1, point2);

    final A = M;
    final B = X2 - X1;
    final C = Y1 - M * X1;

    return Line(x: A, y: B, c: C);
  }

  Line getLineOfSlopeAndPoint(double slope, Point point) {
    double A = slope;
    double B = 1;
    double C = -(slope * point.x - point.y);

    return Line(x: A, y: B, c: C);
  }

  Point getIntersectOf2Lines(Line d1, Line d2) {
    final x = (d1.y * d2.c - d2.y * d1.c) / (d1.x * d2.y - d2.x * d1.y);
    final y = (d2.x * d1.c - d1.x * d2.c) / (d1.x * d2.y - d2.x * d1.y);

    return Point(x: x, y: y);
  }
}

void main() {
  final calculator = Calculator();

  final startPoint = Point(x: -3, y: 3);
  final endPoint = Point(x: 5, y: -1);
  final origin = Point.origin();

  final lineOverOrigin = calculator.getLineOf2Points(startPoint, origin);
  lineOverOrigin.display();

  final slope = calculator.getSlopeOf2Points(startPoint, origin);
  final verticalSlope = -1 / slope;

  final intersectLine = calculator.getLineOfSlopeAndPoint(verticalSlope, endPoint);
  final intersect = calculator.getIntersectOf2Lines(lineOverOrigin, intersectLine);

  intersect.display();
}
