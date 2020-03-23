//
opensdg.dataRounding = function(value) {
  if (value == null) {
    return value
  }
  else {
    //5 555 --> 5 560; 34,56 --> 34,6; 3,4 --> 3,40; 1 --> 1,00
    //return value.toPrecision(3)

    ////5 555 --> 5 555,00; 34,56 --> 34,65; 3,4 --> 3,40; 1 --> 1,00
    //return value.toFixed(2)

    return value
  }
};
