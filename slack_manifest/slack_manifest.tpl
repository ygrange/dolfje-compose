display_information:
  name: Dolfje
features:
  bot_user:
    display_name: Dolfje
    always_online: false
  slash_commands:
$slash_commands
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - channels:history
      - channels:manage
      - chat:write
      - chat:write.public
      - commands
      - groups:write
      - im:write
      - mpim:write
      - users:read
settings:
  event_subscriptions:
    request_url: $event_url
    bot_events:
      - message.channels
  org_deploy_enabled: false
  socket_mode_enabled: false
  token_rotation_enabled: false

