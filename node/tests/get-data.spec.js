var _ = require('lodash');
var getData = require('../lib/get-data');
var sinon = require('sinon');
var expect = require('chai').expect;

var sandbox;

before(function(done){
    sandbox = sinon.sandbox.create();
    done();
});

after(function(done){
    sandbox.restore();
    done();
})

describe('api calls', function () {


    it('should return c20 data', async function () {
        var response = await getData.c20();
        expect(response).to.include.all.keys(['presale', 'holdings']);
    });

    it('should return cmc top 25 data', async function () {
        var response = await getData.cmc();
        console.log('response:', response);
        expect(response.length).to.equal(25)
    });

    it('should call all functions', async function () {
        var c20Spy = sandbox.spy(getData, 'c20');
        var cmcSpy = sandbox.spy(getData, 'cmc');
        await getData.all();
        expect(cmcSpy.called).to.be.true;
        expect(c20Spy.called).to.be.true;
    });

})