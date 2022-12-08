import { config } from "dotenv";

config();

export const PORT = process.env.PORT || 3000


/*
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=diego989
DB_DATABASE=companydb
*/