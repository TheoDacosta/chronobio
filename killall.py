import subprocess

result = subprocess.run(["ps", "aux"], capture_output=True)

stdout = result.stdout.decode("utf-8")
for line in stdout.splitlines():
    if "python" not in line:
        continue
    if "chronobio." in line or "sample_player_client" in line:
        print(line)
        pid = line.split()[1]
        subprocess.run(["kill", "-9", pid], capture_output=True)