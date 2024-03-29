#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  static heights () {
    return this.heigth;
  }

  rotate () {
    const swap = this.height;
    this.height = this.width;
    this.width = swap;
  }
}

module.exports = Rectangle;
