const appDbName = process.env.MONGO_DB_NAME || "inz";
const appUsername = process.env.MONGO_APP_USERNAME || "inz_user";
const appPassword = process.env.MONGO_APP_PASSWORD || "devpass";

db = db.getSiblingDB(appDbName);

db.createUser({
    user: appUsername,
    pwd: appPassword,
    roles: [
        { role: "readWrite", db: appDbName },
        { role: "dbAdmin", db: appDbName }
    ]
});
