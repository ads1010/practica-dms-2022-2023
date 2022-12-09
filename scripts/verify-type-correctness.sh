#!/bin/bash

SUCCESS=0

echo "[dms2223common]"
mypy --install-types --non-interactive components/dms2223common/dms2223common
SUCCESS=$((${SUCCESS}+$?))
echo "[dms2223auth]"
mypy --install-types --non-interactive components/dms2223common/dms2223common components/dms2223auth/dms2223auth
SUCCESS=$((${SUCCESS}+$?))
echo "[dms2223backend]"
mypy --install-types --non-interactive components/dms2223common/dms2223common components/dms2223backend/dms2223backend
SUCCESS=$((${SUCCESS}+$?))
echo "[dms2223frontend]"
mypy --install-types --non-interactive components/dms2223common/dms2223common components/dms2223frontend/dms2223frontend
SUCCESS=$((${SUCCESS}+$?))

exit ${SUCCESS}
