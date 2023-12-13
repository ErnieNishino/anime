// index.js
const animeData = require('../../data/animeData.json'); // 请替换为实际的数据路径

Page({
  data: {
    showAnime: [],
  },
  showAnimeByDay(e) {
    const day = e.currentTarget.dataset.day;
    const filteredAnime = animeData.filter(item => item.updateDay === day);
    this.setData({ showAnime: filteredAnime });
  },
  goToDetailPage(e) {
    const index = e.currentTarget.dataset.index;
    const selectedAnime = this.data.showAnime[index];
    wx.navigateTo({
      url: `/pages/detail/detail?name=${selectedAnime.name}&cover=${selectedAnime.cover}&type=${selectedAnime.type}&actors=${selectedAnime.actors}&production=${selectedAnime.production}`,
    });
  },
});
