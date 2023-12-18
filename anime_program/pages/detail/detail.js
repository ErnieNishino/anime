// detail.js
Page({
  data: {
    Name: null,
    Day: null,
    Type: null,
    Intro: null,
    Actors: null,
    Prod: null,
    Rate: null
  },
  onLoad(options) {
    this.setData({
      Name: options.name,
      Day: options.day,
      Type: options.type,
      Intro: options.intro,
      Actors: options.actors,
      Prod: options.prod,
      Rate: options.rate
    });
  },
  
  navigateBack: function () {
    wx.navigateBack();
  }
});
