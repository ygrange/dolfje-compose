# dolfje-compose
[![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)
## Dolfje
Dolfje a the bot that can be used to play werewolves in a slack space. It has been developed for the MNOT Weerwolven slack. You can find the source code [here|https://github.com/decentaur/dolfje]. We wanted to deploy this bot on the ASTRON slack as a remote fun activity for the SDC team. To do this, we wrapped the bot in a docker-compose file and wrote a (python) script to generate a slack manifest file to make deploying the bot as easy as possible.  

## Usage
*Prerequisites*: A node that will run the bot. The node is expected to be facing the Internet so that slack can communicate with it. Since the slack is using docker compose, the node should be run a Docker deamon and be able to either run `docker-compose` or have te `compose` plugin for Docker installed.

Also it is required that you are allowed to install apps for a slack space. By default all full members can install apps, but this can be limited by the owners and admins of the space. 

The docker-compose file contains the bot, together with its database, and runs the [Traefik|traefik.io] reverse proxy, using the ACME client to automatically manage a TLS certificate for the service. 

### Creating the manifest and the Slack app
The first step to take is to generate a `manifest`, which is a YAML or JSON file describing all properties of the app (e.g. what rights it has in the slack space, what information slack should send to it) so that the app can easily be created on the slack site. In this repository, there is a `python3` script that can be used to generate a YAML manifest. 

To generate the manifest, go to the `slack_manifest` directory. The `make_manifest.py` script takes two command-line arguments: the langugage (`en` or `nl`) and the root URL of the bot (so if you deploy the bot) and execute the script. For instance, if you are planning to execute the bot on URL `https://werewolf.example.com` and want all the commands and descriptions in English, the syntax would be
```
./make_manifest.py en https://werewolf.example.com
```
. After executing this command (and assuming it did not throw an exception), you will find a file `slack_manifest.yml` in the directory containing all information needed to proceeed. 

The slack app needs to be set up in the slack API. The procedure is as follows:
1. In your browser, go to [https://api.slack.com] and click on "Your Apps" (top-right). 
2. Click the (green) "Create New App" button.
3. Click on "From an App manifest".
4. Pick the workspace in which you will be usng Dolfje, click Next.
5. At the top of the edit box, click on `YAML` and paste the contents of the `slack_manifest.yml` we just created, click Next.
6. Check all the data (if you want), and click Create.

This will bring you to the `Basic Information` page. If you scroll down, there will be a box with a `Signing Secret`. The secred in that box (which you can show and copy) is one of the configuratbles that needs to be added to the `.env` file (see below). A bit below you will find a "Display Information" section where you can upload a profile picture to make you bot even more recognisable in your slack space (and a textual description).

If you were to go to your slacp space, you would notice the bot to not be present. This s because the bot has not yet been 'installed'. Please note that every time you change the claims / rights your bot needs to access, you will have to repeat this step (in general, the slack app management pages will explicitly tell you to do this). But now we need to install the app, which will also provide us with the `OAuth token` that we will need to put in the `.env` file (see below).

Click `Oauth & Permission` in the menu on the left. On the page, find `OAuth Tokens for Your Workspace` and click `Install to Workspace`. Now, click `Allow` and upon return, the page will have a box containing the `Oauth token` in the `Bot User OAuth Token` box.

### Running the bot code
Now on the node where the bot will actually run, go to the root directoryu of this repository. You will have to create an environment file. If you use an older version of docker compose (which does _not support_ the `--env-file` flag) this file has to be called `.env`. In the file `example.env` you will find the parameters that you are expected to provide. You can get the `SLACK_SIGNING_SECRET` from the Basic Information page, as mentioned before. The `SLACK_BOT_TOKEN` will take the value of the `Oauth token`. The `APPLANG` is either `en` or `nl` depending on the languate you want the app in (note that some error messages are only implemented in Dutch, so expect some Dutch in the english version). The `SLACK_URL` is the root URL of the bot. The other parameters can be chosen by the user and are described in the example file.

Bringing up the bot is then either
```
docker compose --env-file slack_environment.env up -d
```
(where the env file is called `slack_environment.env`)
or
```
docker-compose up -d
```
(where the env file has to be called `.env`)

Now you are set to go.

## Contributing
If you have comments on this repository, please open an issue in the issue tracker corresponding to the repository. If you want to provide code please submit a pull request on Github (https://www.github.com/ygrange/dolfje-deploy).
