const HelloWorld = artifacts.require("HelloWorld");

contract("HelloWorld", async (accounts) => {
    it("should return 'Hello World!'", async () => {
        let instance = await HelloWorld.deployed();
        let greeting = await instance.sayHello.call();

        assert.equal(greeting, "Hello World!");
    });

    it("should set payload", async () => {
        const payloadString = "This is some data";
        let instance = await HelloWorld.deployed();

        await instance.setPayload(payloadString);
        let payload = await instance.payload.call();

        assert.equal(payload, payloadString);
    });
});
