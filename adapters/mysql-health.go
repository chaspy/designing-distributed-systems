package main

import (
	"database/sql"
	"flag"
	"fmt"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

var (
	user   = flag.String("user", "", "The database user name")
	passwd = flag.String("password", "", "The database password")
	dtbs   = flag.String("database", "", "The database to connect to")
	query  = flag.String("query", "", "The test query")
	addr   = flag.String("address", "localhost:8080", "The address to listen on")
)

// 使用方法:
//   db-check -query="SELECT * from my-cool-table" \
//            -user=bdburns \
//            -password="you wish"
//            -database=dbname
//
func main() {
	flag.Parse()
	db, err := sql.Open("mysql", fmt.Sprintf("%s:%s@/%s", *user, *passwd, *dtbs))
	if err != nil {
		fmt.Printf("Error opening database: %v", err)
	}

	// クエリを実行するシンプルなWebハンドラ
	http.HandleFunc("/", func(res http.ResponseWriter, req *http.Request) {
		_, err := db.Exec(*query)
		if err != nil {
			res.WriteHeader(http.StatusInternalServerError)
			res.Write([]byte(err.Error()))
			return
		}
		res.WriteHeader(http.StatusOK)
		res.Write([]byte("OK"))
		return
	})
	// サーバを起動
	http.ListenAndServe(*addr, nil)
}
