// detail.js
Page({
  data: {
    Name: "暂无",
    Day: "暂无",
    Type: "暂无",
    Intro: "暂无",
    Actors: "暂无",
    Prod: "暂无",
    Rate: "暂无"
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
