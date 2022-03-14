
// Jaden Casing Strings


String.prototype.toJadenCase = function () {
    //...
    var result = this.split(" ")
    newArr = []
      for (string of result){
        newArr.push(string[0].toUpperCase() + string.substring(1))
      }
      return newArr.join(" ")
  };
