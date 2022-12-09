#!/bin/bash

pylint --fail-under=7.0 -f text components/dms2223common/dms2223common components/dms2223auth/dms2223auth components/dms2223backend/dms2223backend components/dms2223frontend/dms2223frontend
