class Mutant {
  constructor(name, power, level) {
    this.name = name;
    this.power = power;
    this.level = level;
  }

  usePower() {
    return `${this.name} uses ${this.power} at level ${this.level}!`;
  }
}

module.exports = Mutant;
