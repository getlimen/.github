# Limen

> *Latin: "threshold"* — the stone at the bottom of a Roman doorway.

**Self-hosted infrastructure in one platform.** Docker deployments, reverse proxy with automatic TLS, and WireGuard VPN — unified under a single admin UI.

## Components

| Repo | Name | Role |
|------|------|------|
| [limen](https://github.com/getlimen/limen) | *Threshold* | Central manager (C# + Angular + PostgreSQL) |
| [ostiarius](https://github.com/getlimen/ostiarius) | *Doorkeeper* | Reverse proxy with auto-TLS (YARP) |
| [forculus](https://github.com/getlimen/forculus) | *Door panel* | WireGuard hub |
| [limentinus](https://github.com/getlimen/limentinus) | *Guardian* | Universal node agent |

## Why Roman doors?

Romans assigned specific deities to each part of a doorway. *Limen* guards the threshold, *Forculus* the door panel, *Limentinus* the threshold itself, and *Ostiarius* the doorkeeper. Each component in our platform mirrors the role of its namesake.

## License

All repositories are [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) licensed.
