# snyk-jira-issues-manager

## Instructions to download snyk binary

### MacOS

```bash
curl https://static.snyk.io/cli/latest/snyk-macos -o snyk
chmod +x ./snyk
mv ./snyk /usr/local/bin/ 
```

### Windows

```
curl https://static.snyk.io/cli/latest/snyk-win.exe -o snyk.exe
```

### Linux

```bash
curl https://static.snyk.io/cli/latest/snyk-linux -o snyk
chmod +x ./snyk
mv ./snyk /usr/local/bin/ 
```

## Authenticating

```bash
snyk auth
```

> Opens a browser window with prompts to log in to your Snyk account and authenticate your machine. No repository permissions are needed at this stage.

# Open Source Scanning

> To scan your open-source packages for vulnerabilities ensure all dependencies are installed or there is a supported lockfile. Then, run:

```bash
snyk monitor --all-projects --org=<org>
```

# Source Code Scanning

> To scan your source code for vulnerabilities, ensure Snyk Code is enabled in Settings > Snyk Code. Then, run:

```bash
snyk code test --org=<org>
```

# Container Scanning

> To scan container images for vulnerabilities copy the command below and specify the container image by replacing <repository> and <tag>.

```bash
snyk container monitor <repository>:<tag> --org=<org>
```

# IaC Scanning

> Scan your Infrastructure as Code (IaC) files for vulnerabilities. Run:

```bash
snyk iac test --report --org=<org>
```

# Free accounts

Free accounts do not get organization API Keys, but they do still get a personal API Key. The Snyk API does not require any encoding to use the authentication method directly (looking at you Jira and SonarQube!) So copy the API Key from your user settings and use it directly as `SNYK_TOKEN` in the code.