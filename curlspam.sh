#!/usr/bin/env bash

URL="http://localhost:8001/api/timeout-request?non_circuit_breaker=true"
# URL="http://localhost:8002/api/timeout-request?non_circuit_breaker=true"
# URL="http://localhost:8001/api/timeout-request"

# seq 1 1000 | xargs -n1 -P20 -I{} \
#   curl -s -o /dev/null -w "[{}] %{http_code}\n" "$URL"

# for i in $(seq 1 200); do curl -s -o /dev/null -w "%{http_code}\n" $URL; done

for i in $(seq 1 200); do
  curl -s -o /dev/null -w "%{http_code} %{time_total}\n" $URL \
  | awk '{printf "%s %.0fms\n",$1,$2*1000}'
done

# seq 200 | xargs -I{} -P16 sh -c \
# "curl -s -o /dev/null -w '%{http_code} %{time_total}\n' $URL  | awk '{printf \"%s %.0fms\\n\",\$1,\$2*1000}'"