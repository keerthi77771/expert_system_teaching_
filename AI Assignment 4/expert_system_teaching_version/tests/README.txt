Test Cases:

1. Input: ['budget_high', 'portable', 'long_battery'] → Expected: recommend:premium_ultrabook
2. Input: ['budget_low', 'office_only', 'portable'] → Expected: recommend:budget_ultrabook
3. Input: ['gaming', 'budget_medium'] → Expected: recommend:midrange_gaming_laptop
4. Input: ['gaming', 'budget_high'] → Expected: recommend:high_end_gaming_laptop
5. Input: ['creative_work', 'portable'] → Expected: spec:ram_16_plus
6. Input: ['creative_work', 'large_screen'] → Expected: spec:display_15_plus_color_accurate
7. Input: ['travel_often', 'long_battery'] → Expected: spec:battery_60wh_plus
8. Input: ['pref_os_macos'] → Expected: spec:macos_required
9. Input: ['pref_os_linux', 'office_only'] → Expected: spec:linux_friendly_hw
10. Input: ['needs_ai_accel'] → Expected: spec:gpu_with_tensor_cores
