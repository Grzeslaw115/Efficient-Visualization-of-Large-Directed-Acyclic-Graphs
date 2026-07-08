const appDbName = process.env.MONGO_DB_NAME || "dagmara";
const appUsername = process.env.MONGO_APP_USERNAME || "dagmara_app";
const appPassword = process.env.MONGO_APP_PASSWORD;

if (!appPassword) {
  throw new Error("MONGO_APP_PASSWORD is required");
}

db = db.getSiblingDB(appDbName);

db.createUser({
    user: appUsername,
    pwd: appPassword,
    roles: [
        { role: "readWrite", db: appDbName }
    ]
});
