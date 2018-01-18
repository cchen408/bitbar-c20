const request = require('request-promise');
var _ = require('lodash');

// which data to grab
const toCall = ['c20', 'cmc'];

module.exports = {

    data: {},

    /**
     * make all the api calls needed and grab all data needed
     * @returns {Promise.<*[]>}
     */
    all: async function () {
        var promises = [];
        var self = this;
        _.each(toCall, function (name) {
            promises.push(self[name]());
        });
        return Promise.all(promises);
    },

    /**
     * api call to get c20 data
     * @returns {Promise.<*>}
     */
    c20: async function () {
        var response = await request({
            method: 'GET',
            url: 'https://crypto20.com/status',
            json: true
        });
        this.data.c20 = response;
        return response;
    },

    /**
     * api call to get coin market cap data
     * @returns {Promise.<void>}
     */
    cmc: async function(){
        var response = await request({
            method: 'GET',
            url: 'https://api.coinmarketcap.com/v1/ticker/?limit=25',
            json: true
        });
        this.data.cmc = response;
        return response;
    }


};