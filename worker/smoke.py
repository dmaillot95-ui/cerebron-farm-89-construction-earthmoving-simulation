import json,math,hashlib,pathlib
mu=3.986004418e14; Re=6378137.0; alt=400000.0; r=Re+alt
v=math.sqrt(mu/r); period=2*math.pi*math.sqrt(r**3/mu); accel=mu/r**2
checks={"finite":all(map(math.isfinite,[v,period,accel])),"positive":min(v,period,accel)>0,"leo_velocity_range":7000<v<8500,"leo_period_range":5000<period<6000}
result={"status":"PASS" if all(checks.values()) else "FAIL","model":"deterministic-dynamics-smoke-v1","inputs":{"mu_m3_s2":mu,"earth_radius_m":Re,"altitude_m":alt},"outputs":{"circular_velocity_m_s":v,"period_s":period,"gravity_m_s2":accel},"checks":checks,"epistemic":"SMOKE_TEST_ONLY_NOT_DOMAIN_CALIBRATED_NOT_PHYSICAL_VALIDATION"}
pathlib.Path("artifacts").mkdir(exist_ok=True); raw=json.dumps(result,sort_keys=True).encode(); result["payload_sha256"]=hashlib.sha256(raw).hexdigest(); pathlib.Path("artifacts/smoke-result.json").write_text(json.dumps(result,indent=2)+"\n"); print(json.dumps(result,indent=2)); raise SystemExit(0 if result["status"]=="PASS" else 1)
