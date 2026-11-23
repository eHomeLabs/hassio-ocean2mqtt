# 0.2.4

- Add Nexelec INSAFE+ Origin / I870EO (D2-14-30): smoke, temperature, humidity, comfort, battery status and diagnostics.
- Add the Community product sheet, generic profile, FR/EN labels and manual-ID onboarding instructions.
- Exclude gateway chip ID and Base ID sender addresses from unknown devices, preserving the raw telegram journal.
- Existing devices, settings and MQTT topics are preserved.

# 0.2.3

- Public FR/EN device catalog with search, filters, pairing instructions and contribution links.
- Interface update detection and explicit reload, with HTML cache prevention.
- Identify generic devices with their real brand/model and photo/manual links, prefilled into test reports.
- Device diagnostics and decoded application telegram values, including CSV.
- Existing data, topics and pairing are preserved.

An older interface must load this version once before it can show future update banners.

# 0.2.1

- Complete EEP profiles in telegrams, search and CSV exports.
- Generic device hardware test reports can create validated brand/model sheets after maintainer review.
- Twelve generic device illustrations with a “générique” badge, automatically used when a product photo is missing or unavailable.
- Keeps the existing configuration and device data.

# 0.2.0

- First stable release of the multi-brand EnOcean to MQTT gateway.
- Keeps the existing add-on slug, configuration and device data when upgrading from 0.2.0b28.
- Includes A5-04-03 temperature and humidity support and GPL v3 information in About.
- Device support levels remain Validated, Community or Generic per catalog entry.

Back up Home Assistant and export an Ocean2MQTT backup before upgrading.
