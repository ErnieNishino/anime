// detail.js
Page({
  data: {
    animeDetail: {},
  },
  onLoad(options) {
    const { name, cover, type, actors, production } = options;
    this.setData({ animeDetail: { name, cover, type, actors, production } });
  },
  navigateBack: function () {
    wx.navigateBack();
  }
});
