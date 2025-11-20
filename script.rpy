





<!DOCTYPE html>
<html
  lang="en"
  
  data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"
  data-a11y-animated-images="system" data-a11y-link-underlines="true"
  
  >

    <style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style>




  <head>
    <meta charset="utf-8">
  <script type="text/javascript" nonce="e3a0b3757c4546ff80e94c0eb3f" src="//local.adguard.org?ts=1763612568318&amp;type=content-script&amp;dmn=github.com&amp;url=https%3A%2F%2Fgithub.com%2Fyukihina%2Fhtl66%2Fblob%2Fclaude%2Fimplement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q%2Fscript.rpy&amp;app=vivaldi.exe&amp;css=2&amp;js=1&amp;rel=1&amp;rji=1&amp;sbe=1&amp;stealth=1&amp;st-wrtc&amp;st-push&amp;st-loc&amp;st-dnt"></script><link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-8e973f836952.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-4bce7af39e21.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-34b642d57214.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-54be93e666a7.css" /><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-8ae7edf5489c.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-84d50df427c0.css" /><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-a80873375146.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-ad512d3e2f3b.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-d152d6cd6879.css" /><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-fa4060c1a9da.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-d7bad0fb00bb.css" /><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-4a0107c0f60c.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-045e6b6ac094.css" /><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-5de537db5e79.css" />

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-15839d47b75d.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-efa08b71f947.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-6dcb16809e76.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-490b3f68bf33.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-5d735668c600.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-9c9b8dc61e74.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_enable_snapshot_keyword","actions_image_version_event","alternate_user_config_repo","api_insights_show_missing_data_banner","attestations_filtering","attestations_sorting","billing_hard_budget_limits_for_licenses","client_version_header","codespaces_prebuild_region_target_update","contentful_lp_footnotes","copilot_agent_cli_public_preview","copilot_agent_task_list_v2","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_api_agentic_issue_marshal_yaml","copilot_api_draft_issues_with_dependencies","copilot_api_github_draft_update_issue_skill","copilot_chat_agents_empty_state","copilot_chat_attach_multiple_images","copilot_chat_disable_model_picker_while_streaming","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_raycast_logo","copilot_file_block_ref_matching","copilot_free_to_paid_telem","copilot_ftp_hyperspace_upgrade_prompt","copilot_ftp_settings_upgrade","copilot_ftp_upgrade_to_pro_from_models","copilot_ftp_your_copilot_settings","copilot_immersive_generate_thread_name_async","copilot_immersive_issues_readonly_viewer","copilot_immersive_issues_show_relationships","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_insights_public_preview","copilot_issue_list_show_more","copilot_org_policy_page_focus_mode","copilot_pipes_code_nodes","copilot_pipes_github_graphql_nodes","copilot_premium_request_quotas","copilot_security_alert_assignee_options","copilot_share_active_subthread","copilot_spaces_as_attachments","copilot_spaces_ga","copilot_spark_empty_state","copilot_spark_loading_webgl","copilot_spark_progressive_error_handling","copilot_spark_use_billing_headers","copilot_stable_conversation_view","copilot_swe_agent_progress_commands","copilot_swe_agent_use_subagents","copilot_workbench_agent_seed_tool","copilot_workbench_agent_user_edit_awareness","copilot_workbench_cache","copilot_workbench_preview_analytics","copilot_workbench_use_single_prompt","data_router_force_refetch_on_navigation","deployment_record_api","direct_to_salesforce","disable_dashboard_universe_2025_private_preview","dom_node_counts","dotcom_chat_client_side_skills","enterprise_ai_controls","failbot_report_error_react_apps_on_page","fetch_graphql_improved_error_serialization","fgpat_permissions_selector_redesign","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","github_models_scheduled_hydro_events","global_search_multi_orgs","global_sso_banner","global_sso_banner_dismiss_dialog","hyperspace_2025_logged_out_batch_1","hyperspace_nudges_universe25","hyperspace_nudges_universe25_post_event","initial_per_page_pagination_updates","inp_reduced_threshold","issue_fields_report_usage","issues_expanded_file_types","issues_lazy_load_comment_box_suggestions","issues_react_blur_item_picker_on_close","issues_react_bots_timeline_pagination","issues_react_include_bots_in_pickers","issues_react_prohibit_title_fallback","issues_react_remove_placeholders","issues_report_sidebar_interactions","issues_sticky_sidebar","issues_template_copilot_assignment","item_picker_label_tsq_migration","item_picker_project_tsq_migration","kb_convert_to_space","kb_semantic_api_migration","lifecycle_label_name_updates","link_contact_sales_swp_marketo","marketing_pages_search_explore_provider","mcp_registry_install","mcp_registry_oss_v0_1_api","memex_default_issue_create_repository","memex_grouped_by_edit_route","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","mission_control_use_body_html","new_traffic_page_banner","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","pinned_issue_fields","pr_sfv_new_diff_fetch","primer_react_segmented_control_tooltip","projects_assignee_max_limit","react_fetch_graphql_ignore_expected_errors","record_sso_banner_metrics","repos_insights_remove_new_url","repository_suggester_elastic_search","ruleset_deletion_confirmation","sample_network_conn_type","scheduled_reminders_updated_limits","site_features_copilot_universe","site_homepage_collaborate_video","site_homepage_contentful","site_homepage_eyebrow_banner","site_homepage_universe_animations","site_msbuild_webgl_hero","spark_agent_max_output_tokens_error","spark_fix_rename","spark_force_push_after_checkout","spark_improve_image_upload","spark_kv_encocoded_keys","spark_show_data_access_on_publish","spark_sync_repository_after_iteration","viewscreen_sandbox","webp_support","workbench_store_readonly"],"login":"yukihina","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-148d4198d00e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/913-ca2305638c53.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/6488-de87864e6818.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/environment-3bc3b3b3a6f6.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/11683-aa3d1ebe6648.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/43784-4652ae97a661.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4712-809eac2badf7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81028-5b8c5e07a4fa.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/74911-6a311b93ee8e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/91853-b5d2e5602241.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/78143-31968346cf4c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/52430-c46e2de36eb2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-5b3e77949adb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-188a1950b315.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/28546-ee41c9313871.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/17688-a9e16fb5ed13.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2869-a4ba8f17edb3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/70191-5122bf27bf3e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7332-5ea4ccf72018.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3200-a7d4487d8022.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/95964-56279d5d08b3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/89708-cf8a683757b8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51519-dc0d4e14166a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/7534-44b89d9287f7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/96384-750ef5263abe.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19718-676a65610616.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-3b0493ae367b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/48011-5b6f71a93de7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-eb21f5b0029d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/53996-5a7cf1bdd2cd.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-26fed944c925.js" defer="defer"></script>
  
  <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/primer-react-1d943c070f89.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-760965ba27bb.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-core-6bff7e7eaf4e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/octicons-react-a215e6ee021a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/58267-d3b3e418eb9c.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/48775-3cc79d2cd30e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/42892-9fe102b0683f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/23832-db66abd83e08.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/99418-9d4961969e0d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/33915-05ba9b3edc31.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/35563-88b5576b2c6b.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/51220-ec5733320b36.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/32219-7472a62a38a8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/83597-a037b23eee45.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/25407-6e094ff52623.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81929-06b7f240be06.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/40771-fd733f45c051.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/66990-26254330a98f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/29665-aafd67585c49.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/19976-d9a685a90a0d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81725-de9dc2dbc3e4.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3774-beb5035d8d47.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/18406-6bc4085c106d.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/36584-798b01636f52.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/29806-d6f60b3ec9f4.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-dd173b9ab390.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/react-code-view.b17093118927c84cf318.module.css" />


  <title>htl66/script.rpy at claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q · yukihina/htl66</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient>
  <meta name="route-controller" content="blob" data-turbo-transient>
  <meta name="route-action" content="show" data-turbo-transient>
  <meta name="fetch-nonce" content="v2:ebedc879-7efb-78a6-3df4-a81a0a4da931">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="604D:31EEAF:28E8A3:37AA04:691EB504" data-turbo-transient="true" /><meta name="html-safe-nonce" content="c2444885d43406a168af90d7a3219b94d4a59785a15e51138777f94d0d2e8c66" data-turbo-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS95dWtpaGluYS9odGw2Ni90cmVlL2NsYXVkZS9pbXBsZW1lbnQtYXV0by1wcm9ncmVzc2lvbi1yYXRlcy0wMTRyVFVTa0J3a3NLcXFWQTQxUnhjNFEiLCJyZXF1ZXN0X2lkIjoiNjA0RDozMUVFQUY6MjhFOEEzOjM3QUEwNDo2OTFFQjUwNCIsInZpc2l0b3JfaWQiOiI0NDg2MDEzODcyNjU1Njk4MzEwIiwicmVnaW9uX2VkZ2UiOiJpYWQiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true" /><meta name="visitor-hmac" content="6f02bcfb783f1f6559ed59eee5f44a64e059864f0a7ba9a99653d48be37e55c9" data-turbo-transient="true" />


    <meta name="hovercard-subject-tag" content="repository:991065825" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" /><meta name="octolytics-actor-id" content="125949572" /><meta name="octolytics-actor-login" content="yukihina" /><meta name="octolytics-actor-hash" content="8ec6e5187f971250e7bf441830b795627b0ea7b1ed7b4fe60b3b129c346efb78" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




    <meta name="user-login" content="yukihina">

  <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Contribute to yukihina/htl66 development by creating an account on GitHub.">

      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/yukihina/htl66/blob/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy" />

      <meta name="twitter:image" content="https://opengraph.githubassets.com/243926f12749dadd5ddc55eab13764dc4ab411b1992d5a60039da7ef0c035534/yukihina/htl66" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="htl66/script.rpy at claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q · yukihina/htl66" /><meta name="twitter:description" content="Contribute to yukihina/htl66 development by creating an account on GitHub." />
  <meta property="og:image" content="https://opengraph.githubassets.com/243926f12749dadd5ddc55eab13764dc4ab411b1992d5a60039da7ef0c035534/yukihina/htl66" /><meta property="og:image:alt" content="Contribute to yukihina/htl66 development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="htl66/script.rpy at claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q · yukihina/htl66" /><meta property="og:url" content="https://github.com/yukihina/htl66/blob/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy" /><meta property="og:description" content="Contribute to yukihina/htl66 development by creating an account on GitHub." />
  


      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/125949572/ws?session=eyJ2IjoiVjMiLCJ1IjoxMjU5NDk1NzIsInMiOjE4NzI4ODMzNzQsImMiOjk2NDQ3ODA5NSwidCI6MTc2MzYyMDEwMX0=--ba54c3e93d121a574dc99c0a6fcf2a8c5e1303b65aee09636e9f5d4669efe853" data-refresh-url="/_alive" data-session-id="7f68057eb558221c99b6366e91daad0367af29b61cf27393b66e085b63e11ed1">
      <link rel="shared-web-socket-src" href="/assets-cdn/worker/socket-worker-2a038060e454.js">


      <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">
      <meta name="hovercards-preference" content="true">
      <meta name="announcement-preference-hovercard" content="true">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="dd1c9334cfef3da7a26099a029581037c1a809fb5dae462915d95ef72df0c211" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="21a43568025709b66240454fc92d4f09335a96863f8ab1c46b4a07f6a5b67102" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="aa39222f646973caef6f9a96a5bf67f2bee1360d5ee8981c0927a9efa873ddf7" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="ef37c147982555efcafcb721b86cfc0341e36ed58e0b2b6b9bdd0447d34a1e60" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/yukihina/htl66 git https://github.com/yukihina/htl66.git">

  <meta name="octolytics-dimension-user_id" content="125949572" /><meta name="octolytics-dimension-user_login" content="yukihina" /><meta name="octolytics-dimension-repository_id" content="991065825" /><meta name="octolytics-dimension-repository_nwo" content="yukihina/htl66" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="991065825" /><meta name="octolytics-dimension-repository_network_root_nwo" content="yukihina/htl66" />



    

    <meta name="turbo-body-classes" content="logged-in env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="039a914add5ccd1652839bfb9464f207ceed2d74">
  <meta name="ui-target" content="canary-1">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;" >
    <div data-turbo-body class="logged-in env-production page-responsive" style="word-wrap: break-word;" >
        <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent></div>
      



    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/keyboard-shortcuts-dialog.29aaeaafa90f007c6f61.module.css" />

<react-partial
  partial-name="keyboard-shortcuts-dialog"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>





      

          

                  <header class="AppHeader" role="banner">
      <h2 class="sr-only">Navigation Menu</h2>


        

        <div class="AppHeader-globalBar pb-2  js-global-bar">
          <div class="AppHeader-globalBar-start responsive-context-region">
            <div class="">
                      <react-partial-anchor>
        <button data-target="react-partial-anchor.anchor" aria-label="Open global navigation menu" show_tooltip="false" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--medium Button p-0 color-fg-muted">  <span class="Button-content">
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg></span>
  </span>
</button>
        <template data-target="react-partial-anchor.template">
          <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/90759.a6b6b0e7cc0a5e5c6f13.module.css" />

<react-partial
  partial-name="global-nav-menu"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"home":{"href":"/dashboard","hotkey":"g d"},"feed":{"show":false,"href":"/feed"},"issues":{"href":"/issues","hotkey":"g i"},"pulls":{"href":"/pulls","hotkey":"g p"},"contributedRepos":{"show":false,"href":null,"hotkey":null},"projects":{"href":"/projects"},"discussions":{"show":true,"href":"/discussions"},"codespaces":{"show":true,"href":"https://github.com/codespaces"},"copilot":{"show":true,"href":"/copilot"},"spark":{"show":false,"href":null},"marketplace":{"show":true,"href":"/marketplace"},"mcp":{"show":true,"href":"https://github.com/mcp"},"explore":{"show":true,"href":"/explore"},"richContent":{"show":true,"contentUrl":"/_side-panels/global.json","repositoriesSearchUrl":"/_side-panel-items/global/repositories.json","teamsSearchUrl":"/_side-panel-items/global/teams.json"}}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>


        </template>
      </react-partial-anchor>

            </div>

            <a class="AppHeader-logo ml-1 "
              href="https://github.com/"
              data-hotkey="g d"
              aria-label="Homepage "
              data-turbo="false"
              data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}"
            >
              <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
            </a>

              <context-region-controller
  class="AppHeader-context responsive-context-region"
  data-max-items="5"
  
>
  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="GitHub Breadcrumb">
      
<context-region data-target="context-region-controller.contextRegion" role="list"  data-action="context-region-changed:context-region-controller#crumbsChanged">
    <context-region-crumb
      data-crumb-id="contextregion-usercrumb-yukihina"
      data-targets="context-region.crumbs"
      data-label="yukihina"
      data-href="/yukihina"
      data-pre-rendered
      role="listitem"
      
    >
      <a data-target="context-region-crumb.linkElement" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;yukihina&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/yukihina/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/yukihina" id="contextregion-usercrumb-yukihina-link" data-view-component="true" class="AppHeader-context-item">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">
          yukihina
        </span>

</a>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered >
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor" />
    </svg>
  </span>
</context-region-divider>

    </context-region-crumb>

      <li data-target="context-region-controller.overflowMenuContainer context-region.overflowMenuContainer" role="listitem" hidden>
        <action-menu data-target="context-region-controller.overflowActionMenu" data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-button" popovertarget="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-overlay" aria-controls="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-list" aria-haspopup="true" aria-labelledby="tooltip-ae8ce715-ddbd-43bf-9419-cb40d37238f9" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-ae8ce715-ddbd-43bf-9419-cb40d37238f9" for="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Show more breadcrumb items</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-overlay" anchor="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list>
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-button" id="action-menu-38107d98-6987-4180-abb8-e3fa3b1af463-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="hidden" data-crumb-id="contextregion-usercrumb-yukihina" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-8f7df78f-fa26-4bdb-89ad-adae8ccdf99a" href="/yukihina" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          yukihina
</span>      
</a>
  
</li>
        <li hidden="hidden" data-crumb-id="contextregion-repositorycrumb-htl66" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-f2fce98e-3437-44f3-bb38-1a783c805aae" href="/yukihina/htl66" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          htl66
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu>
  <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered >
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor" />
    </svg>
  </span>
</context-region-divider>


      </li>
    <context-region-crumb
      data-crumb-id="contextregion-repositorycrumb-htl66"
      data-targets="context-region.crumbs"
      data-label="htl66"
      data-href="/yukihina/htl66"
      data-pre-rendered
      role="listitem"
      
    >
      <a data-target="context-region-crumb.linkElement" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;htl66&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="/yukihina/htl66" id="contextregion-repositorycrumb-htl66-link" data-view-component="true" class="AppHeader-context-item">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">
          htl66
        </span>

</a>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered >
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor" />
    </svg>
  </span>
</context-region-divider>

    </context-region-crumb>

</context-region>

    </nav>
  </div>
</context-region-controller>

          </div>
          <div class="AppHeader-globalBar-end">
              <div class="AppHeader-search" >
                  


<qbsearch-input class="search-input" data-scope="repo:yukihina/htl66" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="Rlc8e3qWdA8iYMiAWl97KMSh2i6CtUdZ5pL7Zb51YpDC8696h0105PvFgsLVwTuWxemDGir1VOwVYxDRQvuAKw" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="yukihina/htl66" data-current-org="" data-current-owner="yukihina" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0"
    data-action="click:qbsearch-input#searchInputContainerClicked"
  >
        
              <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
            </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control AppHeader-search-control-overflow">
      <label
        for="AppHeader-searchInput"
        aria-label="Search or jump to…"
        class="AppHeader-search-visual--leading"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                  <button
              type="button"
              data-target="qbsearch-input.inputButton"
              data-action="click:qbsearch-input#handleExpand"
              class="AppHeader-searchButton form-control text-left color-fg-subtle no-wrap"
              data-hotkey="s,/"
              data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}"
              aria-describedby="search-error-message-flash"
            >
              <div class="overflow-hidden">
                <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                    Type <kbd class="AppHeader-search-kbd">/</kbd> to search
                </span>
              </div>
            </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay>
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container"
          style="border-radius: 12px;"
          data-target="qbsearch-input.queryBuilderContainer"
          hidden
        >
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="query-builder-test-form" action="" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div
        class="QueryBuilder-StyledInput width-fit "
        data-target="query-builder.styledInput"
      >
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div
            aria-hidden="true"
            class="QueryBuilder-StyledInputContent"
            data-target="query-builder.styledInputContent"
          ></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-62b3e23e-92a2-40e3-94e8-66c2aaf096b7" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="hidden" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</template>

<template id="code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="file-code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-code">
    <path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
</template>

<template id="history-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
</svg>
</template>

<template id="repo-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</template>

<template id="bookmark-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bookmark">
    <path d="M3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 0 1-1.227.579L8 11.722l-3.773 3.107A.751.751 0 0 1 3 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.91l3.023-2.489a.75.75 0 0 1 .954 0l3.023 2.49V2.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="plus-circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus-circle">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7.25-3.25v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
</template>

<template id="trash-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path>
</svg>
</template>

<template id="team-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
</template>

<template id="project-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
</template>

<template id="pencil-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
</template>

<template id="copilot-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="copilot-error-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot-error">
    <path d="M16 11.24c0 .112-.072.274-.21.467L13 9.688V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-.198 0-.388-.009-.571-.029L6.833 5.226a4.01 4.01 0 0 0 .17-.782c.117-.935-.037-1.395-.241-1.614-.193-.206-.637-.413-1.682-.297-.683.076-1.115.231-1.395.415l-1.257-.91c.579-.564 1.413-.877 2.485-.996 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095Zm-5.083-8.707c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Zm2.511 11.074c-1.393.776-3.272 1.428-5.43 1.428-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.18-.455-.241-.963-.252-1.475L.31 4.107A.747.747 0 0 1 0 3.509V3.49a.748.748 0 0 1 .625-.73c.156-.026.306.047.435.139l14.667 10.578a.592.592 0 0 1 .227.264.752.752 0 0 1 .046.249v.022a.75.75 0 0 1-1.19.596Zm-1.367-.991L5.635 7.964a5.128 5.128 0 0 1-.889.073c-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433 1.539 0 3.089-.505 4.063-.934Z"></path>
</svg>
</template>

<template id="workflow-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-workflow">
    <path d="M0 1.75C0 .784.784 0 1.75 0h3.5C6.216 0 7 .784 7 1.75v3.5A1.75 1.75 0 0 1 5.25 7H4v4a1 1 0 0 0 1 1h4v-1.25C9 9.784 9.784 9 10.75 9h3.5c.966 0 1.75.784 1.75 1.75v3.5A1.75 1.75 0 0 1 14.25 16h-3.5A1.75 1.75 0 0 1 9 14.25v-.75H5A2.5 2.5 0 0 1 2.5 11V7h-.75A1.75 1.75 0 0 1 0 5.25Zm1.75-.25a.25.25 0 0 0-.25.25v3.5c0 .138.112.25.25.25h3.5a.25.25 0 0 0 .25-.25v-3.5a.25.25 0 0 0-.25-.25Zm9 9a.25.25 0 0 0-.25.25v3.5c0 .138.112.25.25.25h3.5a.25.25 0 0 0 .25-.25v-3.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="book-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
</template>

<template id="code-review-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-review">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 13H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25v-8.5C0 1.784.784 1 1.75 1ZM1.5 2.75v8.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Zm5.28 1.72a.75.75 0 0 1 0 1.06L5.31 7l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.75.75 0 0 1 1.06 0Zm2.44 0a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L10.69 7 9.22 5.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="codespaces-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
</template>

<template id="comment-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment">
    <path d="M1 2.75C1 1.784 1.784 1 2.75 1h10.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 13.25 12H9.06l-2.573 2.573A1.458 1.458 0 0 1 4 13.543V12H2.75A1.75 1.75 0 0 1 1 10.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h4.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="comment-discussion-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</template>

<template id="organization-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</template>

<template id="rocket-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-rocket">
    <path d="M14.064 0h.186C15.216 0 16 .784 16 1.75v.186a8.752 8.752 0 0 1-2.564 6.186l-.458.459c-.314.314-.641.616-.979.904v3.207c0 .608-.315 1.172-.833 1.49l-2.774 1.707a.749.749 0 0 1-1.11-.418l-.954-3.102a1.214 1.214 0 0 1-.145-.125L3.754 9.816a1.218 1.218 0 0 1-.124-.145L.528 8.717a.749.749 0 0 1-.418-1.11l1.71-2.774A1.748 1.748 0 0 1 3.31 4h3.204c.288-.338.59-.665.904-.979l.459-.458A8.749 8.749 0 0 1 14.064 0ZM8.938 3.623h-.002l-.458.458c-.76.76-1.437 1.598-2.02 2.5l-1.5 2.317 2.143 2.143 2.317-1.5c.902-.583 1.74-1.26 2.499-2.02l.459-.458a7.25 7.25 0 0 0 2.123-5.127V1.75a.25.25 0 0 0-.25-.25h-.186a7.249 7.249 0 0 0-5.125 2.123ZM3.56 14.56c-.732.732-2.334 1.045-3.005 1.148a.234.234 0 0 1-.201-.064.234.234 0 0 1-.064-.201c.103-.671.416-2.273 1.15-3.003a1.502 1.502 0 1 1 2.12 2.12Zm6.94-3.935c-.088.06-.177.118-.266.175l-2.35 1.521.548 1.783 1.949-1.2a.25.25 0 0 0 .119-.213ZM3.678 8.116 5.2 5.766c.058-.09.117-.178.176-.266H3.309a.25.25 0 0 0-.213.119l-1.2 1.95ZM12 5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
</template>

<template id="shield-check-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield-check">
    <path d="m8.533.133 5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667l5.25-1.68a1.748 1.748 0 0 1 1.066 0Zm-.61 1.429.001.001-5.25 1.68a.251.251 0 0 0-.174.237V7c0 1.36.275 2.666 1.057 3.859.784 1.194 2.121 2.342 4.366 3.298a.196.196 0 0 0 .154 0c2.245-.957 3.582-2.103 4.366-3.297C13.225 9.666 13.5 8.358 13.5 7V3.48a.25.25 0 0 0-.174-.238l-5.25-1.68a.25.25 0 0 0-.153 0ZM11.28 6.28l-3.5 3.5a.75.75 0 0 1-1.06 0l-1.5-1.5a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l.97.97 2.97-2.97a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
</template>

<template id="heart-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
</template>

<template id="server-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-server">
    <path d="M1.75 1h12.5c.966 0 1.75.784 1.75 1.75v4c0 .372-.116.717-.314 1 .198.283.314.628.314 1v4a1.75 1.75 0 0 1-1.75 1.75H1.75A1.75 1.75 0 0 1 0 12.75v-4c0-.358.109-.707.314-1a1.739 1.739 0 0 1-.314-1v-4C0 1.784.784 1 1.75 1ZM1.5 2.75v4c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25Zm.25 5.75a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25ZM7 4.75A.75.75 0 0 1 7.75 4h4.5a.75.75 0 0 1 0 1.5h-4.5A.75.75 0 0 1 7 4.75ZM7.75 10h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1 0-1.5ZM3 4.75A.75.75 0 0 1 3.75 4h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 4.75ZM3.75 10h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</template>

<template id="globe-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-globe">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM5.78 8.75a9.64 9.64 0 0 0 1.363 4.177c.255.426.542.832.857 1.215.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a9.927 9.927 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.507 6.507 0 0 0 4.666 5.5c-.123-.181-.24-.365-.352-.552-.715-1.192-1.437-2.874-1.581-4.948Zm-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948.12-.197.237-.381.353-.552a6.507 6.507 0 0 0-4.666 5.5Zm10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948-.12.197-.237.381-.353.552a6.507 6.507 0 0 0 4.666-5.5Zm2.733-1.5a6.507 6.507 0 0 0-4.666-5.5c.123.181.24.365.353.552.714 1.192 1.436 2.874 1.58 4.948Z"></path>
</svg>
</template>

<template id="issue-opened-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</template>

<template id="device-mobile-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-device-mobile">
    <path d="M3.75 0h8.5C13.216 0 14 .784 14 1.75v12.5A1.75 1.75 0 0 1 12.25 16h-8.5A1.75 1.75 0 0 1 2 14.25V1.75C2 .784 2.784 0 3.75 0ZM3.5 1.75v12.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM8 13a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
</template>

<template id="package-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-package">
    <path d="m8.878.392 5.25 3.045c.54.314.872.89.872 1.514v6.098a1.75 1.75 0 0 1-.872 1.514l-5.25 3.045a1.75 1.75 0 0 1-1.756 0l-5.25-3.045A1.75 1.75 0 0 1 1 11.049V4.951c0-.624.332-1.201.872-1.514L7.122.392a1.75 1.75 0 0 1 1.756 0ZM7.875 1.69l-4.63 2.685L8 7.133l4.755-2.758-4.63-2.685a.248.248 0 0 0-.25 0ZM2.5 5.677v5.372c0 .09.047.171.125.216l4.625 2.683V8.432Zm6.25 8.271 4.625-2.683a.25.25 0 0 0 .125-.216V5.677L8.75 8.432Z"></path>
</svg>
</template>

<template id="credit-card-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-credit-card">
    <path d="M10.75 9a.75.75 0 0 0 0 1.5h1.5a.75.75 0 0 0 0-1.5h-1.5Z"></path><path d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25ZM14.5 6.5h-13v5.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Zm0-2.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25V5h13Z"></path>
</svg>
</template>

<template id="play-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
</template>

<template id="gift-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
</template>

<template id="code-square-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
</template>

<template id="device-desktop-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-device-desktop">
    <path d="M14.25 1c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 14.25 12h-3.727c.099 1.041.52 1.872 1.292 2.757A.752.752 0 0 1 11.25 16h-6.5a.75.75 0 0 1-.565-1.243c.772-.885 1.192-1.716 1.292-2.757H1.75A1.75 1.75 0 0 1 0 10.25v-7.5C0 1.784.784 1 1.75 1ZM1.75 2.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25ZM9.018 12H6.982a5.72 5.72 0 0 1-.765 2.5h3.566a5.72 5.72 0 0 1-.765-2.5Z"></path>
</svg>
</template>

        <div class="position-relative">
                <ul
                  role="listbox"
                  class="ActionListWrap QueryBuilder-ListWrap"
                  aria-label="Suggestions"
                  data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  "
                  data-target="query-builder.resultsList"
                  data-persist-list=false
                  id="query-builder-test-results"
                  tabindex="-1"
                ></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-62b3e23e-92a2-40e3-94e8-66c2aaf096b7" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="zN18nEqu5-2H43iw-DPLbj2-rzU18tKIK2r3f8m2XLCKunpJpkdS8ElSoB3ACm95BDINUokF0wcSdbAo_Y2SAw" />
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="FkiV-mu8TuIHUesNKf2hVrMV2iukqJGyrxMtUq0F-eb89w8qUOXUge3sAL46zyvi-rYTeHUF7uG4JpK0pieRPg" />
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required>
              <input
                type="text"
                name="custom_scope_name"
                id="custom_scope_name"
                data-target="custom-scopes.customScopesNameField"
                class="form-control"
                autocomplete="off"
                placeholder="github-ruby"
                required
                maxlength="50">
              <input type="hidden" value="BZx2oXbZVjeUFJGTPjZNuIeppGpBZhc4M44vwbjgaYj24kzs-Z9auhS7rteRnr0sPCKn3L2pe1F4CKVmae9iUw" data-csrf="true" />
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input
              type="text"
              name="custom_scope_query"
              id="custom_scope_query"
              data-target="custom-scopes.customScopesQueryField"
              class="form-control"
              autocomplete="off"
              placeholder="(repo:mona/a OR repo:mona/b) AND lang:python"
              required
              maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="rlr2mquMncMZssDPrBNJhSHNKTg1oGXwXGNBjKbacQHbtmUJ0z6ET7_OKIF9V8Adi8IcWiDaK5fknNIpoG1VDw" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />


              </div>

            
              <div class="AppHeader-CopilotChat hide-sm hide-md">
  <div class="d-flex">
    <react-partial-anchor>
        <a href="/copilot" data-target="react-partial-anchor.anchor" id="copilot-chat-header-button" aria-labelledby="tooltip-b62f1bf9-0ab8-4793-9e3a-a673e0fa60fb" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonLeft cursor-wait">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot Button-visual">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-b62f1bf9-0ab8-4793-9e3a-a673e0fa60fb" for="copilot-chat-header-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Chat with Copilot</tool-tip>

      <template data-target="react-partial-anchor.template">
        <script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/18312-17646a9d1ca3.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/40420-d22dc985a766.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/347-d8794b0e68a7.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/52049-aa86186cd7dd.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/37051-cb8690bd8a08.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/62318-1533a458c2ff.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/30997-43b688803191.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/3025-0e441b2f6975.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/11048-7bcc0c218a96.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/37294-84593db7c295.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/30721-5cbde854429a.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/2635-bb0b392d182e.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/81171-0132ed576c5f.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/10306-91ddc9fd9e15.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/4817-8a2689aded16.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/28902-06cf38827ce2.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/36982-2ff55885e9dc.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/92687-ecd4570b9154.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/34031-80252173b2e1.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/29405-7f915c510db8.js" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="https://github.githubassets.com/assets/copilot-chat-7269c872c82d.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/29405.8b7bba9eb72962481d6b.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/copilot-chat.588a40d6c4d417bb8182.module.css" />
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/copilot-markdown-rendering-ddd978d4a7c0.css" />
        <include-fragment src="/github-copilot/chat?skip_anchor=true" data-nonce="v2:ebedc879-7efb-78a6-3df4-a81a0a4da931" data-view-component="true">
  
  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>
      </template>
    </react-partial-anchor>
    <div class="position-relative">
      
        <react-partial-anchor>
          <button id="global-copilot-menu-button" data-target="react-partial-anchor.anchor" aria-expanded="false" aria-labelledby="tooltip-25b6a7f5-b8bd-4c1e-93f4-6a80c56554a5" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonRight">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-25b6a7f5-b8bd-4c1e-93f4-6a80c56554a5" for="global-copilot-menu-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Open Copilot…</tool-tip>

          <template data-target="react-partial-anchor.template">
            <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-copilot-menu.9d926f69ee309a45d0df.module.css" />

<react-partial
  partial-name="global-copilot-menu"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"repository":{"id":991065825,"name":"htl66","ownerLogin":"yukihina"}}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>


          </template>
        </react-partial-anchor>
    </div>
  </div>
</div>


            <div class="AppHeader-actions position-relative">
                 <react-partial-anchor>
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" disabled="disabled" data-view-component="true" class="AppHeader-button AppHeader-button--dropdown global-create-button cursor-wait Button--secondary Button--medium Button width-auto color-fg-muted">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-6c15eaec-f8ec-4838-937f-35125e1a08d9" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Create new…</tool-tip>

      <template data-target="react-partial-anchor.template">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-create-menu.30736d4aa7b2b246dd6f.module.css" />

<react-partial
  partial-name="global-create-menu"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"showCreateRepo":true,"showImportRepo":true,"showCodespaces":true,"showSpark":false,"showCodingAgent":false,"showGist":true,"showCreateOrg":true,"showCreateProject":false,"showCreateLegacyProject":false,"showCreateIssue":true,"createProjectUrl":"/yukihina?tab=projects","org":null,"owner":"yukihina","repo":"htl66"}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>


      </template>
    </react-partial-anchor>


                <a href="/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-3def6412-82c6-465b-9432-e3c1525f686f" aria-labelledby="tooltip-a945f5a7-a339-4431-9d23-1131cc2c6b68" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-a945f5a7-a339-4431-9d23-1131cc2c6b68" for="icon-button-3def6412-82c6-465b-9432-e3c1525f686f" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Your issues</tool-tip>

                <a href="/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-69ab3728-773b-475f-b193-efcab0eb3713" aria-labelledby="tooltip-0d7fa138-79db-457b-bc49-2664190903d7" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-0d7fa138-79db-457b-bc49-2664190903d7" for="icon-button-69ab3728-773b-475f-b193-efcab0eb3713" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Your pull requests</tool-tip>

            </div>

              <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTI1OTQ5NTcyIiwidCI6MTc2MzYyMDEwMX0=--2fadc083d58675512a3032448fb75bb072c191851fcdd863ef8d11474b3ac3ea" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel">
    <a id="AppHeader-notifications-button" href="/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:null}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Notifications</tool-tip>
</notification-indicator>

            <div class="AppHeader-user">
              <deferred-side-panel data-url="/_side-panels/user?repository_id=991065825">
  <include-fragment data-target="deferred-side-panel.fragment" data-nonce="v2:ebedc879-7efb-78a6-3df4-a81a0a4da931" data-view-component="true">
  
    <react-partial-anchor
  
>
  <button data-target="react-partial-anchor.anchor" data-login="yukihina" aria-label="Open user navigation menu" type="button" data-view-component="true" class="cursor-wait Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0">  <span class="Button-content">
    <span class="Button-label"><img src="https://avatars.githubusercontent.com/u/125949572?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" /></span>
  </span>
</button>
  <template data-target="react-partial-anchor.template">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react.1880ae4a0cc8c9bf298c.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-user-nav-drawer.90949a46e3c775d67262.module.css" />

<react-partial
  partial-name="global-user-nav-drawer"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"yukihina","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/125949572?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2Fyukihina%2Fhtl66%2Fblob%2Fclaude%2Fimplement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q%2Fscript.rpy","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/yukihina?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>


  </template>
</react-partial-anchor>


  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment></deferred-side-panel>
            </div>

            <div class="position-absolute mt-2">
                
<site-header-logged-in-user-menu>

</site-header-logged-in-user-menu>

            </div>
          </div>
        </div>


        
            <div class="AppHeader-localBar" >
              <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/yukihina/htl66/tree/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /yukihina/htl66/tree/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/yukihina/htl66/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /yukihina/htl66/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/yukihina/htl66/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /yukihina/htl66/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/yukihina/htl66/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /yukihina/htl66/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/yukihina/htl66/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /yukihina/htl66/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="wiki-tab" href="/yukihina/htl66/wiki" data-tab-item="i5wiki-tab" data-selected-links="repo_wiki /yukihina/htl66/wiki" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g w" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Wiki&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        <span data-content="Wiki">Wiki</span>
          <span id="wiki-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/yukihina/htl66/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /yukihina/htl66/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/yukihina/htl66/security/overall-count" accept="text/fragment+html" data-nonce="v2:ebedc879-7efb-78a6-3df4-a81a0a4da931" data-view-component="true">
  
  <div data-show-on-forbidden-error hidden>
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        <p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="" aria-label="Please reload this page">Please reload this page</a>.</p>
</p>

</div>  </div>
</div>  </div>
</include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/yukihina/htl66/pulse" data-tab-item="i7insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /yukihina/htl66/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="settings-tab" href="/yukihina/htl66/settings" data-tab-item="i8settings-tab" data-selected-links="code_review_limits code_quality codespaces_repository_settings collaborators custom_tabs github_models_repo_settings hooks integration_installations interaction_limits issue_template_editor key_links_settings license_policy notifications repo_announcements repo_branch_settings repo_custom_properties repo_keys_settings repo_pages_settings repo_protected_tags_settings repo_rule_insights repo_rules_bypass_requests repo_rulesets repo_settings_copilot_coding_guidelines repo_settings_copilot_content_exclusion repo_settings_copilot_swe_agent repo_settings reported_content repository_actions_settings_add_new_runner repository_actions_settings_general repository_actions_settings_runner_details repository_actions_settings_runners repository_actions_settings repository_environments role_details secrets_settings_actions secrets_settings_codespaces secrets_settings_dependabot secrets security_analysis security_products /yukihina/htl66/settings" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Settings&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        <span data-content="Settings">Settings</span>
          <span id="settings-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <button id="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-button" popovertarget="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-overlay" aria-controls="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-list" aria-haspopup="true" aria-labelledby="tooltip-5a58b68f-0fa1-4dd1-8ce3-43c114fd69c8" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-5a58b68f-0fa1-4dd1-8ce3-43c114fd69c8" for="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-overlay" anchor="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list>
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-button" id="action-menu-3e1a31ce-c24e-4d59-bd61-5932337c689d-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="hidden" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-83985525-d160-4dd5-bf5b-347d276baccf" href="/yukihina/htl66/tree/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-85b4f02c-aeca-489f-bdb1-c851a62c34e1" href="/yukihina/htl66/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-e0a5c7f1-641b-47ac-98c0-fd772e3af879" href="/yukihina/htl66/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-c50fb7d4-12e2-47db-88b9-ad2cd46ce51b" href="/yukihina/htl66/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-b105c496-29fd-4774-952a-66b619fbd528" href="/yukihina/htl66/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i5wiki-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-46662125-89a6-4e1d-abe6-11554abf4b75" href="/yukihina/htl66/wiki" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Wiki
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i6security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-df41f9fb-6a00-4d55-b45f-0ba3f15a2b3f" href="/yukihina/htl66/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i7insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-e1c4cce0-a1f0-4dcd-a12f-f222916817bb" href="/yukihina/htl66/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
        <li hidden="hidden" data-menu-item="i8settings-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-183fa988-f86b-4e30-9488-870e76fd8722" href="/yukihina/htl66/settings" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
              
            </div>
    </header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden>You switched accounts on another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>

    <button id="icon-button-e40a72d1-f592-4c7e-8c63-5da338e8b132" aria-labelledby="tooltip-fb64299b-129f-4d64-bfea-474787f05cb5" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-fb64299b-129f-4d64-bfea-474787f05cb5" for="icon-button-e40a72d1-f592-4c7e-8c63-5da338e8b132" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace>




  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div >
    <button autofocus class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    <div aria-atomic="true" role="alert" class="js-flash-alert">
      
      <div>{{ message }}</div>

    </div>
  </div>
</div>
  </template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTI1OTQ5NTcyIiwidCI6MTc2MzYyMDEwMX0=--2fadc083d58675512a3032448fb75bb072c191851fcdd863ef8d11474b3ac3ea" data-view-component="true" class="js-socket-channel"></notification-shelf-watcher>
  <div hidden data-initial data-target="notification-shelf-watcher.placeholder"></div>






  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
    data-project-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" >
      
      






    
  <div id="repository-container-header" data-turbo-replace hidden ></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content " >
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="/codespaces/new/yukihina/htl66/tree/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q?resume=1">Open in codespace</a>




    
      
    








<react-app
  app-name="react-code-view"
  initial-path="/yukihina/htl66/blob/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy"
    style="display: block; min-height: calc(100vh - 64px);"
  data-attempted-ssr="true"
  data-ssr="true"
  data-lazy="false"
  data-alternate="false"
  data-data-router-enabled="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":".vscode","path":".vscode","contentType":"directory"},{"name":"3dcamera","path":"3dcamera","contentType":"directory"},{"name":"cache","path":"cache","contentType":"directory"},{"name":"fonts","path":"fonts","contentType":"directory"},{"name":"saves","path":"saves","contentType":"directory"},{"name":"scripts","path":"scripts","contentType":"directory"},{"name":"tl","path":"tl","contentType":"directory"},{"name":".gitattributes","path":".gitattributes","contentType":"file"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"ACHIEVEMENTS_SYSTEM_DOCUMENTATION.md","path":"ACHIEVEMENTS_SYSTEM_DOCUMENTATION.md","contentType":"file"},{"name":"AUDIO_SYSTEM_DOCUMENTATION.md","path":"AUDIO_SYSTEM_DOCUMENTATION.md","contentType":"file"},{"name":"CHARACTER_INFO_DOCUMENTATION.md","path":"CHARACTER_INFO_DOCUMENTATION.md","contentType":"file"},{"name":"CORE_SYSTEM_DOCUMENTATION.md","path":"CORE_SYSTEM_DOCUMENTATION.md","contentType":"file"},{"name":"NOTIFICATIONS_SYSTEM_DOCUMENTATION.md","path":"NOTIFICATIONS_SYSTEM_DOCUMENTATION.md","contentType":"file"},{"name":"PHONE_SYSTEM_DOCUMENTATION.md","path":"PHONE_SYSTEM_DOCUMENTATION.md","contentType":"file"},{"name":"README.txt","path":"README.txt","contentType":"file"},{"name":"STATS_SCREEN_DOCUMENTATION.md","path":"STATS_SCREEN_DOCUMENTATION.md","contentType":"file"},{"name":"changelog.log","path":"changelog.log","contentType":"file"},{"name":"gui.rpy","path":"gui.rpy","contentType":"file"},{"name":"options.rpy","path":"options.rpy","contentType":"file"},{"name":"patch.rpy","path":"patch.rpy","contentType":"file"},{"name":"qori_toolkit_config.ini","path":"qori_toolkit_config.ini","contentType":"file"},{"name":"screens.rpy","path":"screens.rpy","contentType":"file"},{"name":"script.rpy","path":"script.rpy","contentType":"file"},{"name":"work_sessions.json","path":"work_sessions.json","contentType":"file"},{"name":"wt_core.rpy","path":"wt_core.rpy","contentType":"file"},{"name":"wt_ep01.rpy","path":"wt_ep01.rpy","contentType":"file"},{"name":"wt_ep02.rpy","path":"wt_ep02.rpy","contentType":"file"},{"name":"wt_ep03.rpy","path":"wt_ep03.rpy","contentType":"file"},{"name":"wt_ep04.rpy","path":"wt_ep04.rpy","contentType":"file"},{"name":"wt_ep05.rpy","path":"wt_ep05.rpy","contentType":"file"}],"totalCount":31}},"fileTreeProcessingTime":25.416837,"foldersToFetch":[],"incompleteFileTree":false,"repo":{"id":991065825,"defaultBranch":"main","name":"htl66","ownerLogin":"yukihina","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2025-05-26T23:38:36.000-05:00","ownerAvatar":"https://avatars.githubusercontent.com/u/125949572?v=4","public":true,"private":false,"isOrgOwned":false},"codeLineWrapEnabled":false,"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q","listCacheKey":"v0:1763618853.0","canEdit":true,"refType":"branch","currentOid":"3b760886a9a95b8aa6486cd89f95e573c06dfda0","canEditOnDefaultBranch":false,"fileExistsOnDefault":true},"path":"script.rpy","currentUser":{"id":125949572,"login":"yukihina","userEmail":"itabashi.yukana59@gmail.com"},"blob":{"rawLines":["﻿init:","    default persistent.effectsOn = True","    define _scene_show_hide_transition = Dissolve(0.35)","    default mc_name = \"\"","    default walkthrough_enabled = False","    default persistent.walkthrough_all = False","    default persistent.walkthrough_li = set()","    default persistent.disclaimer = False","    default htl_episodes = 6.1","    default rm = RM()","    default ss = SexStats()","","    # Persistent path lock variables for Milestone Decision System","    # Values: \"love\", \"corruption\", \"neutral\", or None (unlocked)","    default persistent.amber_path = None","    default persistent.nanami_path = None","    default persistent.elizabeth_path = None","    default persistent.isabella_path = None","    default persistent.kanae_path = None","    default persistent.arlette_path = None","    default persistent.antonella_path = None","    default persistent.madison_path = None","    default persistent.paz_path = None","","","################################################################################","## MILESTONE DECISION SYSTEM - Episode 6+ Path Locking","################################################################################","## These counters track significant path-defining choices for each character","## When a counter reaches a threshold (typically 3), the character's path locks","","# Amber milestone counters","default amber_love_choices = 0","default amber_cor_choices = 0","","# Nanami milestone counters","default nanami_love_choices = 0","default nanami_cor_choices = 0","","# Elizabeth milestone counters","default elizabeth_love_choices = 0","default elizabeth_cor_choices = 0","","# Isabella milestone counters","default isabella_love_choices = 0","default isabella_cor_choices = 0","","# Kanae milestone counters","default kanae_love_choices = 0","default kanae_cor_choices = 0","","# Arlette milestone counters","default arlette_love_choices = 0","default arlette_cor_choices = 0","","# Antonella milestone counters","default antonella_love_choices = 0","default antonella_cor_choices = 0","","# Madison milestone counters","default madison_love_choices = 0","default madison_cor_choices = 0","","# Paz milestone counters","default paz_love_choices = 0","default paz_cor_choices = 0","","","################################################################################","## SAVE SYSTEM VERSION - For Migration Tracking","################################################################################","## Version 1: Original system without automatic progression rates (default for old saves)","## Version 2: New system with automatic character progression rate multipliers","default save_system_version = 1","","","init python:","    def show_walkthrough(key):","        if walkthrough_enabled and renpy.loadable(\"wt_core.rpyc\"):","            if walkthrough_all:","                messages = []","                for option in walkthrough_data.get(key, {}):","                    if option != \"all\":","                        messages.append(walkthrough_data[key][option])","                message = \" \".join(messages)","            else:","                message = \"\"","                for option in walkthrough_li:","                    if option in walkthrough_data.get(key, {}):","                        message += walkthrough_data[key][option] + \" \"","","            if message:","                renpy.show_screen(\"walkthrough_screen\", message=message)","","    def update_htl_episodes():","        global htl_episodes","        if not htl_episodes == 6.1:","            htl_episodes = 6.1","","label splashscreen:","    scene black","    show nl_bg with clouds_inverse_simple","    $ renpy.pause(0.1, hard=True)","    $ setChannelVolume(channel=\"sfx\", subchannel=5, volume=0.5)","    $ playAudio(sfx_logo_brush, \"sfx\", 5, False, fadein=0, fadeout=0)","    show nl_lo:","            yalign 0.30","            xalign 0.5","    with horicolor_simple","    $ setChannelVolume(channel=\"sfx\", subchannel=8, volume=0.5)","    $ playAudio(sfx_logo, \"sfx\", 8, False, fadein=0, fadeout=0)","    show nl_qo at bounce with bubbles_simple","    show nl_ga at neon_flicker, concentrate, sway with bubbles_simple","    show nl_jp at dizzyness with cwside_simple","    $ setChannelVolume(channel=\"sfx\", subchannel=2, volume=0.5)","    $ playAudio(sfx_logo_jp, \"sfx\", 2, False, fadein=0, fadeout=0)","    $ renpy.pause(3, hard=True)","    scene black with clouds_simple","    $ stopAllSubchannels(channel=\"sfx\", fadeout=0.3)","    $ renpy.pause(0.3, hard=True)","    $ resetAllVolumes()","    return","","","label get_player_name:","    # Asking for the player's name","    $ mc_name = renpy.input(\"What is your name?\", default=\"Chris\", length=20).strip()","    $ mc_name = mc_name if mc_name else \"Chris\"","    ","    return","","","","label start:","    $ update_htl_episodes()","    $ save_system_version = 2  # New games start with version 2 (automatic progression rates)","    stop music fadeout 0.5","    if not persistent.disclaimer:","        $ persistent.disclaimer = True","        call screen confirm_first_time(message=\"This R+ rated game contains explicit sexual content, strong language, graphic violence, and adult themes. All characters are fictional and 18+. Player discretion is advised.\", yes_action=Return())","    else:","        pass","    scene black with smoke","    pause 0.5","    $ playAudio(sfx_hospital_hall, \"amb\", 1, True, 1, 0)","    call showNoise(0.1, 0.15, transition=dissolve)","    show namechg01 with bubbles","    \"Nurse\" \"Good morning!\"","    \"Nurse\" \"I hope you're feeling better today. We've got most of the boring paperwork out of the way, thanks to that gorgeous companion of yours.\"","    \"Nurse\" \"We just need you to confirm your name for our records. Think you can manage that for me?\"","    \"You\" \"Sure...\"","    $ show_custom_notification(\"start_tip\")","    show namechg02","    \"Nurse\" \"I must say, your companion has been incredibly attentive in filling out your information.\"","    \"Nurse\" \"It's not often we see such dedication around here.\"","    \"Girl\" \"Oh, it's the least I could do for him.\"","    \"You\" \"I really appreciate it, thank you both.\"","    show namechg03 with smoke","    \"You\" \"My name... that's all that's left, huh? Everything else has been... handled.\"","    call get_player_name","    mc_t \"Alright. It's [mc_name] then.\"","    scene black with watercolor","    $ stopAllSubchannels(channel=\"amb\", fadeout=1)","    pause 1","    call hideNoise(transition=dissolve)","    jump ep01_title","    return","","label after_load:","    call hideNoise(transition=dissolve)","    $ update_htl_episodes()","","    python:","        try:","","            global patched, patch_activated","            ","","            if renpy.persistent.patch_applied:","                patch_activated = True","                patched = True","","            elif renpy.loadable(\"patch.rpyc\"):","                patch_activated = True","                patched = True","                renpy.persistent.patch_applied = True","            ","            if patched:","                characters = define_characters(True)","                relationships = define_relationships(True)","                globals().update(characters)","                globals().update(relationships)","        except:","            pass","","    # Migrate old saves to new emotional lock system","    python:","        # Migrate RM class to include emotionally_locked field","        if hasattr(store, 'rm'):","            rm.migrate_old_saves()","","        # Check and apply emotional locks for characters with 3 strikes","        for char in [\"amber\", \"nanami\", \"elizabeth\", \"isabella\", \"kanae\",","                     \"arlette\", \"antonella\", \"madison\", \"paz\"]:","            strikes = ss.get(char, \"strike\")","            if strikes \u003e= 3:","                rm.check_emotional_lock(char)","","    # Migrate old saves to new automatic progression rate system","    # Uses \"!= 2\" check to detect any save without the version 2 \"seal\"","    if save_system_version != 2:","        scene black with dissolve","","        centered \"{b}Character Progression System Updated{/b}\\n\\nWe've implemented an automatic character progression rate system\\nto make stat changes more consistent and balanced.\\n\\n{color=#ffcc00}Your save will be automatically migrated.{/color}\\n\\nNote: Due to technical limitations, the migration may not be 100%% perfect.\\nFor the best experience, we recommend starting a new playthrough.\\n\\nPress any key to continue...\"","","        $ renpy.pause(hard=True)","","        # Perform the migration","        $ rm.migrate_to_ratio_system()","        $ save_system_version = 2  # Apply version 2 \"seal\"","","        centered \"{b}Migration Complete{/b}\\n\\nYour character stats have been adjusted to the new system.\\nFuture stat changes will use automatic progression rates.\\n\\nPress any key to continue...\"","","        $ renpy.pause(hard=True)","","    return"],"stylingDirectives":null,"colorizedLines":["\u003cspan class=\"pl-k\"\u003einit\u003c/span\u003e:","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.effectsOn \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefine\u003c/span\u003e _scene_show_hide_transition \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e Dissolve(\u003cspan class=\"pl-c1\"\u003e0.35\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e mc_name \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e walkthrough_enabled \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.walkthrough_all \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.walkthrough_li \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eset\u003c/span\u003e()","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.disclaimer \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e htl_episodes \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6.1\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e rm \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e RM()","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e ss \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e SexStats()","","    \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Persistent path lock variables for Milestone Decision System\u003c/span\u003e","    \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Values: \u0026quot;love\u0026quot;, \u0026quot;corruption\u0026quot;, \u0026quot;neutral\u0026quot;, or None (unlocked)\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.amber_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.nanami_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.elizabeth_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.isabella_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.kanae_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.arlette_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.antonella_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.madison_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e persistent.paz_path \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eNone\u003c/span\u003e","","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e###############################################################################\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e# MILESTONE DECISION SYSTEM - Episode 6+ Path Locking\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e###############################################################################\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e# These counters track significant path-defining choices for each character\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e# When a counter reaches a threshold (typically 3), the character\u0026#39;s path locks\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Amber milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e amber_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e amber_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Nanami milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e nanami_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e nanami_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Elizabeth milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e elizabeth_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e elizabeth_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Isabella milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e isabella_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e isabella_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Kanae milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e kanae_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e kanae_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Arlette milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e arlette_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e arlette_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Antonella milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e antonella_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e antonella_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Madison milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e madison_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e madison_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Paz milestone counters\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e paz_love_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e paz_cor_choices \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e","","","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e###############################################################################\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e# SAVE SYSTEM VERSION - For Migration Tracking\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e###############################################################################\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e# Version 1: Original system without automatic progression rates (default for old saves)\u003c/span\u003e","\u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e# Version 2: New system with automatic character progression rate multipliers\u003c/span\u003e","\u003cspan class=\"pl-k\"\u003edefault\u003c/span\u003e save_system_version \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e","","","\u003cspan class=\"pl-k\"\u003einit\u003c/span\u003e \u003cspan class=\"pl-k\"\u003epython\u003c/span\u003e:","    \u003cspan class=\"pl-k\"\u003edef\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eshow_walkthrough\u003c/span\u003e(\u003cspan class=\"pl-smi\"\u003ekey\u003c/span\u003e):","        \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e walkthrough_enabled \u003cspan class=\"pl-k\"\u003eand\u003c/span\u003e renpy.loadable(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003ewt_core.rpyc\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e):","            \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e walkthrough_all:","                messages \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e []","                \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e option \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e walkthrough_data.get(\u003cspan class=\"pl-k\"\u003ekey\u003c/span\u003e, {}):","                    \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e option \u003cspan class=\"pl-k\"\u003e!=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eall\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e:","                        messages.append(walkthrough_data[\u003cspan class=\"pl-k\"\u003ekey\u003c/span\u003e][option])","                message \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e \u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e.join(messages)","            \u003cspan class=\"pl-k\"\u003eelse\u003c/span\u003e:","                message \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","                \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e option \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e walkthrough_li:","                    \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e option \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e walkthrough_data.get(\u003cspan class=\"pl-k\"\u003ekey\u003c/span\u003e, {}):","                        message \u003cspan class=\"pl-k\"\u003e+=\u003c/span\u003e walkthrough_data[\u003cspan class=\"pl-k\"\u003ekey\u003c/span\u003e][option] \u003cspan class=\"pl-k\"\u003e+\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e \u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","","            \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e message:","                renpy.show_screen(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003ewalkthrough_screen\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003emessage\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003emessage)","","    \u003cspan class=\"pl-k\"\u003edef\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eupdate_htl_episodes\u003c/span\u003e():","        \u003cspan class=\"pl-k\"\u003eglobal\u003c/span\u003e htl_episodes","        \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enot\u003c/span\u003e htl_episodes \u003cspan class=\"pl-k\"\u003e==\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6.1\u003c/span\u003e:","            htl_episodes \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e6.1\u003c/span\u003e","","\u003cspan class=\"pl-k\"\u003elabel\u003c/span\u003e \u003cspan class=\"pl-en\"\u003esplashscreen\u003c/span\u003e:","    \u003cspan class=\"pl-k\"\u003escene\u003c/span\u003e black","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e nl_bg \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e clouds_inverse_simple","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e renpy.pause(\u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003ehard\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e setChannelVolume(\u003cspan class=\"pl-smi\"\u003echannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003esubchannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003evolume\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e playAudio(sfx_logo_brush, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e5\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadein\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadeout\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e nl_lo:","            \u003cspan class=\"pl-e\"\u003eyalign\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.30\u003c/span\u003e","            \u003cspan class=\"pl-e\"\u003exalign\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e horicolor_simple","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e setChannelVolume(\u003cspan class=\"pl-smi\"\u003echannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003esubchannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003evolume\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e playAudio(sfx_logo, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e8\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadein\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadeout\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e nl_qo \u003cspan class=\"pl-k\"\u003eat\u003c/span\u003e bounce \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e bubbles_simple","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e nl_ga \u003cspan class=\"pl-k\"\u003eat\u003c/span\u003e neon_flicker, concentrate, sway \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e bubbles_simple","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e nl_jp \u003cspan class=\"pl-k\"\u003eat\u003c/span\u003e dizzyness \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e cwside_simple","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e setChannelVolume(\u003cspan class=\"pl-smi\"\u003echannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003esubchannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003evolume\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e playAudio(sfx_logo_jp, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eFalse\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadein\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadeout\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e renpy.pause(\u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003ehard\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003escene\u003c/span\u003e black \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e clouds_simple","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e stopAllSubchannels(\u003cspan class=\"pl-smi\"\u003echannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003esfx\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadeout\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e0.3\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e renpy.pause(\u003cspan class=\"pl-c1\"\u003e0.3\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003ehard\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e resetAllVolumes()","    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e","","","\u003cspan class=\"pl-k\"\u003elabel\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eget_player_name\u003c/span\u003e:","    \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Asking for the player\u0026#39;s name\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e mc_name \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e renpy.input(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eWhat is your name?\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003edefault\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eChris\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003elength\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e20\u003c/span\u003e).strip()","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e mc_name \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e mc_name \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e mc_name \u003cspan class=\"pl-k\"\u003eelse\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eChris\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    ","    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e","","","","\u003cspan class=\"pl-k\"\u003elabel\u003c/span\u003e \u003cspan class=\"pl-en\"\u003estart\u003c/span\u003e:","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e update_htl_episodes()","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e save_system_version \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e  \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e New games start with version 2 (automatic progression rates)\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003estop\u003c/span\u003e \u003cspan class=\"pl-k\"\u003emusic\u003c/span\u003e fadeout \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-k\"\u003enot\u003c/span\u003e persistent.disclaimer:","        \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e persistent.disclaimer \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","        \u003cspan class=\"pl-k\"\u003ecall\u003c/span\u003e \u003cspan class=\"pl-k\"\u003escreen\u003c/span\u003e confirm_first_time(\u003cspan class=\"pl-smi\"\u003emessage\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eThis R+ rated game contains explicit sexual content, strong language, graphic violence, and adult themes. All characters are fictional and 18+. Player discretion is advised.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003eyes_action\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003eReturn())","    \u003cspan class=\"pl-k\"\u003eelse\u003c/span\u003e:","        \u003cspan class=\"pl-k\"\u003epass\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003escene\u003c/span\u003e black \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e smoke","    \u003cspan class=\"pl-k\"\u003epause\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e0.5\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e playAudio(sfx_hospital_hall, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eamb\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e0\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003ecall\u003c/span\u003e showNoise(\u003cspan class=\"pl-c1\"\u003e0.1\u003c/span\u003e, \u003cspan class=\"pl-c1\"\u003e0.15\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003etransition\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003edissolve)","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e namechg01 \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e bubbles","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eNurse\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eGood morning!\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eNurse\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eI hope you\u0026#39;re feeling better today. We\u0026#39;ve got most of the boring paperwork out of the way, thanks to that gorgeous companion of yours.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eNurse\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eWe just need you to confirm your name for our records. Think you can manage that for me?\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eYou\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eSure...\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e show_custom_notification(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003estart_tip\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e namechg02","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eNurse\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eI must say, your companion has been incredibly attentive in filling out your information.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eNurse\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eIt\u0026#39;s not often we see such dedication around here.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eGirl\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eOh, it\u0026#39;s the least I could do for him.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eYou\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eI really appreciate it, thank you both.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003eshow\u003c/span\u003e namechg03 \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e smoke","    \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eYou\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eMy name... that\u0026#39;s all that\u0026#39;s left, huh? Everything else has been... handled.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003ecall\u003c/span\u003e get_player_name","    mc_t \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eAlright. It\u0026#39;s \u003cspan class=\"pl-c1\"\u003e[mc_name]\u003c/span\u003e then.\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003escene\u003c/span\u003e black \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e watercolor","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e stopAllSubchannels(\u003cspan class=\"pl-smi\"\u003echannel\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eamb\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-smi\"\u003efadeout\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e)","    \u003cspan class=\"pl-k\"\u003epause\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e1\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003ecall\u003c/span\u003e hideNoise(\u003cspan class=\"pl-smi\"\u003etransition\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003edissolve)","    \u003cspan class=\"pl-k\"\u003ejump\u003c/span\u003e ep01_title","    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e","","\u003cspan class=\"pl-k\"\u003elabel\u003c/span\u003e \u003cspan class=\"pl-en\"\u003eafter_load\u003c/span\u003e:","    \u003cspan class=\"pl-k\"\u003ecall\u003c/span\u003e hideNoise(\u003cspan class=\"pl-smi\"\u003etransition\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003edissolve)","    \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e update_htl_episodes()","","    \u003cspan class=\"pl-k\"\u003epython\u003c/span\u003e:","        \u003cspan class=\"pl-k\"\u003etry\u003c/span\u003e:","","            \u003cspan class=\"pl-k\"\u003eglobal\u003c/span\u003e patched, patch_activated","            ","","            \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e renpy.persistent.patch_applied:","                patch_activated \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","                patched \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","","            \u003cspan class=\"pl-k\"\u003eelif\u003c/span\u003e renpy.loadable(\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003epatch.rpyc\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e):","                patch_activated \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","                patched \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","                renpy.persistent.patch_applied \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e","            ","            \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e patched:","                characters \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e define_characters(\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","                relationships \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e define_relationships(\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","                \u003cspan class=\"pl-c1\"\u003eglobals\u003c/span\u003e().update(characters)","                \u003cspan class=\"pl-c1\"\u003eglobals\u003c/span\u003e().update(relationships)","        \u003cspan class=\"pl-k\"\u003eexcept\u003c/span\u003e:","            \u003cspan class=\"pl-k\"\u003epass\u003c/span\u003e","","    \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Migrate old saves to new emotional lock system\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003epython\u003c/span\u003e:","        \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Migrate RM class to include emotionally_locked field\u003c/span\u003e","        \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003ehasattr\u003c/span\u003e(store, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026#39;\u003c/span\u003erm\u003cspan class=\"pl-pds\"\u003e\u0026#39;\u003c/span\u003e\u003c/span\u003e):","            rm.migrate_old_saves()","","        \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Check and apply emotional locks for characters with 3 strikes\u003c/span\u003e","        \u003cspan class=\"pl-k\"\u003efor\u003c/span\u003e char \u003cspan class=\"pl-k\"\u003ein\u003c/span\u003e [\u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eamber\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003enanami\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eelizabeth\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eisabella\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003ekanae\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e,","                     \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003earlette\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003eantonella\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003emadison\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003epaz\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e]:","            strikes \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e ss.get(char, \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003estrike\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e)","            \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e strikes \u003cspan class=\"pl-k\"\u003e\u0026gt;=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e3\u003c/span\u003e:","                rm.check_emotional_lock(char)","","    \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Migrate old saves to new automatic progression rate system\u003c/span\u003e","    \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Uses \u0026quot;!= 2\u0026quot; check to detect any save without the version 2 \u0026quot;seal\u0026quot;\u003c/span\u003e","    \u003cspan class=\"pl-k\"\u003eif\u003c/span\u003e save_system_version \u003cspan class=\"pl-k\"\u003e!=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e:","        \u003cspan class=\"pl-k\"\u003escene\u003c/span\u003e black \u003cspan class=\"pl-k\"\u003ewith\u003c/span\u003e dissolve","","        centered \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e{b}\u003c/span\u003eCharacter Progression System Updated\u003cspan class=\"pl-c1\"\u003e{/b}\u003c/span\u003e\u003cspan class=\"pl-cce\"\u003e\\n\\n\u003c/span\u003eWe\u0026#39;ve implemented an automatic character progression rate system\u003cspan class=\"pl-cce\"\u003e\\n\u003c/span\u003eto make stat changes more consistent and balanced.\u003cspan class=\"pl-cce\"\u003e\\n\\n\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e{color=#ffcc00}\u003c/span\u003eYour save will be automatically migrated.\u003cspan class=\"pl-c1\"\u003e{/color}\u003c/span\u003e\u003cspan class=\"pl-cce\"\u003e\\n\\n\u003c/span\u003eNote: Due to technical limitations, the migration may not be 100%% perfect.\u003cspan class=\"pl-cce\"\u003e\\n\u003c/span\u003eFor the best experience, we recommend starting a new playthrough.\u003cspan class=\"pl-cce\"\u003e\\n\\n\u003c/span\u003ePress any key to continue...\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","","        \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e renpy.pause(\u003cspan class=\"pl-smi\"\u003ehard\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","","        \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Perform the migration\u003c/span\u003e","        \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e rm.migrate_to_ratio_system()","        \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e save_system_version \u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e \u003cspan class=\"pl-c1\"\u003e2\u003c/span\u003e  \u003cspan class=\"pl-c\"\u003e\u003cspan class=\"pl-c\"\u003e#\u003c/span\u003e Apply version 2 \u0026quot;seal\u0026quot;\u003c/span\u003e","","        centered \u003cspan class=\"pl-s\"\u003e\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003e{b}\u003c/span\u003eMigration Complete\u003cspan class=\"pl-c1\"\u003e{/b}\u003c/span\u003e\u003cspan class=\"pl-cce\"\u003e\\n\\n\u003c/span\u003eYour character stats have been adjusted to the new system.\u003cspan class=\"pl-cce\"\u003e\\n\u003c/span\u003eFuture stat changes will use automatic progression rates.\u003cspan class=\"pl-cce\"\u003e\\n\\n\u003c/span\u003ePress any key to continue...\u003cspan class=\"pl-pds\"\u003e\u0026quot;\u003c/span\u003e\u003c/span\u003e","","        \u003cspan class=\"pl-k\"\u003e$\u003c/span\u003e renpy.pause(\u003cspan class=\"pl-smi\"\u003ehard\u003c/span\u003e\u003cspan class=\"pl-k\"\u003e=\u003c/span\u003e\u003cspan class=\"pl-c1\"\u003eTrue\u003c/span\u003e)","","    \u003cspan class=\"pl-k\"\u003ereturn\u003c/span\u003e"],"csv":null,"csvError":null,"copilotSWEAgentEnabled":false,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/yukihina/htl66/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"script.rpy","displayUrl":"https://github.com/yukihina/htl66/blob/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy?raw=true","headerInfo":{"blobSize":"8.32 KB","deleteTooltip":"Delete this file","editTooltip":"Edit this file","ghDesktopPath":"x-github-client://openRepo/https://github.com/yukihina/htl66?branch=claude%2Fimplement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q\u0026filepath=script.rpy","isGitLfs":false,"onBranch":true,"shortPath":"9918421","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fyukihina%2Fhtl66%2Fblob%2Fclaude%2Fimplement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q%2Fscript.rpy","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"226","truncatedSloc":"185"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplate":null,"discussionTemplate":null,"language":"Ren'Py","languageID":322,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/yukihina/htl66/blob/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/yukihina/htl66/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/yukihina/htl66/raw/refs/heads/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":4,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":true,"symbols":[]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"copilotSpacesEnabled":false,"modelsAccessAllowed":false,"modelsRepoIntegrationEnabled":false,"isMarketplaceEnabled":true,"csrf_tokens":{"/yukihina/htl66/branches":{"post":"o_uB8pmjVwXOalXwMugWaYhJrhwpfvNERw6WOA30wl8WE0Knj0tVY739bbx9y-9FgZsvliyhDser4s50r_6PIw"},"/repos/preferences":{"post":"K5CWaqYQ0jxBZXwtM-Oh0CcvCJ_yzookA6IONqnYiEV4A5tm3-JapHn9dvOXyHr3uxDBeIqlbRCZRfJRz-myJw"}}},"title":"htl66/script.rpy at claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q · yukihina/htl66","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-0cea8c6113ab.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-105a4a160ddd.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":true,"accessible_code_button":true}}}</script>
  <div data-target="react-app.reactRoot"><style data-styled="true" data-styled-version="5.3.11">.jmjlbk{width:100%;}/*!sc*/
@media screen and (min-width:544px){.jmjlbk{width:100%;}}/*!sc*/
@media screen and (min-width:768px){.jmjlbk{width:auto;}}/*!sc*/
.cIRiaH{max-height:100%;height:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
@media screen and (max-width:768px){.cIRiaH{display:none;}}/*!sc*/
@media screen and (min-width:768px){.cIRiaH{max-height:100vh;height:100vh;}}/*!sc*/
.fvNWEZ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;margin-bottom:16px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
@media screen and (max-width:768px){.bCYVKR{display:none;}}/*!sc*/
.cybVuK{margin-left:auto;margin-right:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-bottom:40px;max-width:100%;margin-top:0;}/*!sc*/
.gSjuRy{display:inherit;}/*!sc*/
.kfsEDb{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:16px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.eLrlvS{max-width:100%;}/*!sc*/
.fNzIif{max-width:100%;list-style:none;display:inline-block;}/*!sc*/
.iRLfgU{display:inline-block;max-width:100%;}/*!sc*/
.jyTWxL{margin-left:16px;margin-right:16px;}/*!sc*/
.hGzGyY{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;}/*!sc*/
.cJXRZE{width:100%;height:-webkit-fit-content;height:-moz-fit-content;height:fit-content;min-width:0;margin-right:0;}/*!sc*/
.fpyUWF{height:40px;padding-left:4px;padding-bottom:16px;}/*!sc*/
.iafbuG{top:0px;z-index:4;background:var(--bgColor-default,var(--color-canvas-default));position:-webkit-sticky;position:sticky;}/*!sc*/
.iNRqcN{display:none;min-width:0;padding-top:8px;padding-bottom:8px;}/*!sc*/
.igwLyx{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:14px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.koZdcA{border-radius:6px 6px 0px 0px;}/*!sc*/
.dIDnLY{border:1px solid;border-top:none;border-color:var(--borderColor-default,var(--color-border-default,#30363d));border-radius:0px 0px 6px 6px;min-width:273px;}/*!sc*/
.hhuNfn{background-color:var(--bgColor-default,var(--color-canvas-default));border:0px;border-width:0;border-radius:0px 0px 6px 6px;padding:0;min-width:0;margin-top:46px;}/*!sc*/
.hNuvaP{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;padding-top:8px;padding-bottom:8px;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;min-width:0;position:relative;}/*!sc*/
.kBkfpQ{position:relative;}/*!sc*/
.lnfLer{-webkit-flex:1;-ms-flex:1;flex:1;position:relative;min-width:0;}/*!sc*/
.djZnHX{tab-size:4;isolation:isolate;position:relative;overflow:auto;max-width:unset;}/*!sc*/
.vdPNv{position:fixed;top:0;right:0;height:100%;width:15px;-webkit-transition:-webkit-transform 0.3s;-webkit-transition:transform 0.3s;transition:transform 0.3s;z-index:1;}/*!sc*/
.vdPNv:hover{-webkit-transform:scaleX(1.5);-ms-transform:scaleX(1.5);transform:scaleX(1.5);}/*!sc*/
data-styled.g1[id="Box-sc-62in7e-0"]{content:"jmjlbk,cIRiaH,fvNWEZ,bCYVKR,cybVuK,gSjuRy,kfsEDb,eLrlvS,fNzIif,iRLfgU,jyTWxL,hGzGyY,cJXRZE,fpyUWF,iafbuG,iNRqcN,igwLyx,koZdcA,dIDnLY,hhuNfn,hNuvaP,kBkfpQ,lnfLer,djZnHX,vdPNv,"}/*!sc*/
.hfSsoj[data-size="medium"][data-no-visuals]{display:none;}/*!sc*/
.eNrdFK[data-size="small"]{color:var(--fgColor-default,var(--color-fg-default,#e6edf3));display:none;}/*!sc*/
@media screen and (min-width:544px){.eNrdFK[data-size="small"]{display:none;}}/*!sc*/
@media screen and (min-width:768px){.eNrdFK[data-size="small"]{display:none;}}/*!sc*/
@media screen and (min-width:1012px){.eNrdFK[data-size="small"]{display:none;}}/*!sc*/
@media screen and (min-width:1280px){.eNrdFK[data-size="small"]{display:block;}}/*!sc*/
data-styled.g16[id="Button__StyledButtonComponent-sc-vqy3e4-0"]{content:"hfSsoj,eNrdFK,"}/*!sc*/
.dWfbpP{font-size:16px;margin-left:8px;}/*!sc*/
.hJQQvf{font-weight:600;display:inline-block;max-width:100%;font-size:16px;}/*!sc*/
.cGzJbh{font-weight:600;display:inline-block;max-width:100%;font-size:14px;}/*!sc*/
data-styled.g24[id="Heading-sc-1vc165i-0"]{content:"dWfbpP,hJQQvf,cGzJbh,"}/*!sc*/
.bWhDnA[data-size="medium"][data-no-visuals]{border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.gXjFlG[data-size="small"][data-no-visuals]{border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.gRAczH[data-size="small"][data-no-visuals]:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.gRAczH[data-size="small"][data-no-visuals]:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.gRAczH[data-size="small"][data-no-visuals]:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
data-styled.g25[id="IconButton__StyledIconButton-sc-i53dt6-0"]{content:"bWhDnA,gXjFlG,gRAczH,"}/*!sc*/
.htWjsS{font-weight:600;}/*!sc*/
data-styled.g27[id="Link__StyledLink-sc-1syctfj-0"]{content:"htWjsS,"}/*!sc*/
.iwmTUC linkButtonSx:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iwmTUC linkButtonSx:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iwmTUC linkButtonSx:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
data-styled.g28[id="LinkButton-sc-1v6zkmg-0"]{content:"iwmTUC,"}/*!sc*/
.xsVwu{padding-left:4px;padding-right:4px;font-weight:400;color:var(--fgColor-muted,var(--color-fg-muted,#848d97));font-size:16px;}/*!sc*/
.iHrMHQ{padding-left:4px;padding-right:4px;font-weight:400;color:var(--fgColor-muted,var(--color-fg-muted,#848d97));font-size:14px;}/*!sc*/
data-styled.g38[id="Text__StyledText-sc-1klmep6-0"]{content:"xsVwu,iHrMHQ,"}/*!sc*/
</style><meta name="github-code-view-meta-stats" id="github-code-view-meta-stats" data-hydrostats="publish"/> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot-1zlEO"><div class="prc-PageLayout-PageLayoutWrapper-s2ao4" data-width="full"><div class="prc-PageLayout-PageLayoutContent-jzDMn"><div tabindex="0" class="Box-sc-62in7e-0 jmjlbk"><div class="prc-PageLayout-PaneWrapper-nGO0U ReposFileTreePane-module__Pane--D26Sw ReposFileTreePane-module__HidePaneWithTreeOverlay--CJn2n" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="prc-PageLayout-HorizontalDivider-CYLp5 prc-PageLayout-PaneHorizontalDivider-4exOb" data-variant-regular="none" data-variant-narrow="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-Vl5LI" data-resizable="true" style="--spacing:var(--spacing-none);--pane-min-width:256px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));--pane-width-size:var(--pane-width-large);--pane-width:320px"><div class="react-tree-pane-contents-3-panel"><div id="repos-file-tree" class="Box-sc-62in7e-0 cIRiaH"><div class="ReposFileTreePane-module__Box_1--ZT_4S"><div class="Box-sc-62in7e-0 fvNWEZ"><h2 class="use-tree-pane-module__Heading--iI_ad prc-Heading-Heading-6CmGO"><button type="button" aria-label="Expand file tree" data-testid="expand-file-tree-button-mobile" class="prc-Button-ButtonBase-c50BI ExpandFileTreeButton-module__Button_1--g8F6Q" data-loading="false" data-size="medium" data-variant="invisible" aria-describedby=":Rl6mplab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-c50BI position-relative ExpandFileTreeButton-module__expandButton--oKI1R ExpandFileTreeButton-module__filesButtonBreakpoint--03FKA fgColor-muted prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-describedby=":R756mplab:-loading-announcement" aria-labelledby=":R156mplab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="se" aria-hidden="true" id=":R156mplab:">Collapse file tree</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><h2 class="Heading-sc-1vc165i-0 dWfbpP">Files</h2></div><div class="ReposFileTreePane-module__Box_2--RgzGf"><div class="ReposFileTreePane-module__Box_3--XDLn8"><div class="ReposFileTreePane-module__FullWidthButtonGroup--avF6A prc-ButtonGroup-ButtonGroup-vcMeG"><div><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R6m6mplab:-loading-announcement" aria-labelledby=":Rm6mplab:" href="/yukihina/htl66/blob/main/script.rpy" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.78 12.78a.75.75 0 0 1-1.06 0L4.47 8.53a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L6.06 8l3.72 3.72a.75.75 0 0 1 0 1.06Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="s" aria-hidden="true" id=":Rm6mplab:">View file on default branch</span></div><div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q branch" data-testid="anchor-button" class="prc-Button-ButtonBase-c50BI react-repos-tree-pane-ref-selector width-full ref-selector-class RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn--D34zl" data-loading="false" data-size="medium" data-variant="default" aria-describedby="ref-picker-repos-header-ref-selector-loading-announcement" id="ref-picker-repos-header-ref-selector"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer--mCbv8"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader--D4cnZ"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer--yO402"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText--bxVhQ"> <!-- -->claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div><div class="ReposFileTreePane-module__Box_4--TLAAU"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ReposFileTreePane-module__IconButton--fpuBk prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R6q6mplab:-loading-announcement" aria-labelledby=":Rq6mplab:" href="/yukihina/htl66/new/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":Rq6mplab:">Add file</span><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 bWhDnA SearchButton-module__IconButton--kxA3Q prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rra6mplab:-loading-announcement" aria-labelledby=":R3a6mplab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R3a6mplab:">Search this repository</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div><div class="Box-sc-62in7e-0 bCYVKR ReposFileTreePane-module__FileResultsList--YEf_n"><span class="TextInput__StyledTextInput-sc-ttxlvl-0 d-flex FileResultsList-module__FilesSearchBox--fSAh3 TextInput-wrapper prc-components-TextInputWrapper-i1ofR prc-components-TextInputBaseWrapper-ueK9q" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id=":R5amplab:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autoCorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":R5amplab: :R5amplabH1:" data-component="input" class="prc-components-Input-Ic-y8" value=""/><span class="TextInput-icon" id=":R5amplabH1:" aria-hidden="true"><kbd>t</kbd></span></span></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div class="Box-sc-62in7e-0 bCYVKR ReposFileTreePane-module__Box_5--cckih"><div class="react-tree-show-tree-items"><div class="ReposFileTreeView-module__Box--bDodO" data-testid="repos-file-tree-container"><nav aria-label="File Tree Navigation"><span class="prc-src-InternalVisuallyHidden-nlR9R" role="status" aria-live="polite" aria-atomic="true"></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-eZtxW"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id=".vscode-item" role="treeitem" aria-labelledby=":R3pimplab:" aria-describedby=":R3pimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R3pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R3pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>.vscode</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="3dcamera-item" role="treeitem" aria-labelledby=":R5pimplab:" aria-describedby=":R5pimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R5pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R5pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>3dcamera</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="cache-item" role="treeitem" aria-labelledby=":R7pimplab:" aria-describedby=":R7pimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R7pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R7pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>cache</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="fonts-item" role="treeitem" aria-labelledby=":R9pimplab:" aria-describedby=":R9pimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R9pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R9pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>fonts</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="saves-item" role="treeitem" aria-labelledby=":Rbpimplab:" aria-describedby=":RbpimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rbpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RbpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>saves</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="scripts-item" role="treeitem" aria-labelledby=":Rdpimplab:" aria-describedby=":RdpimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rdpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RdpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>scripts</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="tl-item" role="treeitem" aria-labelledby=":Rfpimplab:" aria-describedby=":RfpimplabH1:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-gWUdE prc-TreeView-TreeViewItemToggleHover-nEgP- prc-TreeView-TreeViewItemToggleEnd-t-AEB"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rfpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RfpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-PHbeP"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>tl</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id=".gitattributes-item" role="treeitem" aria-labelledby=":Rhpimplab:" aria-describedby=":RhpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rhpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RhpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>.gitattributes</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id=".gitignore-item" role="treeitem" aria-labelledby=":Rjpimplab:" aria-describedby=":RjpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rjpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RjpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="ACHIEVEMENTS_SYSTEM_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":Rlpimplab:" aria-describedby=":RlpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rlpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RlpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>ACHIEVEMENTS_SYSTEM_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="AUDIO_SYSTEM_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":Rnpimplab:" aria-describedby=":RnpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rnpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RnpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>AUDIO_SYSTEM_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="CHARACTER_INFO_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":Rppimplab:" aria-describedby=":RppimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rppimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RppimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>CHARACTER_INFO_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="CORE_SYSTEM_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":Rrpimplab:" aria-describedby=":RrpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rrpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RrpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>CORE_SYSTEM_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="NOTIFICATIONS_SYSTEM_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":Rtpimplab:" aria-describedby=":RtpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rtpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RtpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>NOTIFICATIONS_SYSTEM_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="PHONE_SYSTEM_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":Rvpimplab:" aria-describedby=":RvpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rvpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":RvpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>PHONE_SYSTEM_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="README.txt-item" role="treeitem" aria-labelledby=":R11pimplab:" aria-describedby=":R11pimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R11pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R11pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>README.txt</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="STATS_SCREEN_DOCUMENTATION.md-item" role="treeitem" aria-labelledby=":R13pimplab:" aria-describedby=":R13pimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R13pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R13pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>STATS_SCREEN_DOCUMENTATION.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="changelog.log-item" role="treeitem" aria-labelledby=":R15pimplab:" aria-describedby=":R15pimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R15pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R15pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>changelog.log</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="gui.rpy-item" role="treeitem" aria-labelledby=":R17pimplab:" aria-describedby=":R17pimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R17pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R17pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>gui.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="options.rpy-item" role="treeitem" aria-labelledby=":R19pimplab:" aria-describedby=":R19pimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R19pimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R19pimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>options.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="patch.rpy-item" role="treeitem" aria-labelledby=":R1bpimplab:" aria-describedby=":R1bpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1bpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1bpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>patch.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="qori_toolkit_config.ini-item" role="treeitem" aria-labelledby=":R1dpimplab:" aria-describedby=":R1dpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1dpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1dpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>qori_toolkit_config.ini</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="screens.rpy-item" role="treeitem" aria-labelledby=":R1fpimplab:" aria-describedby=":R1fpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1fpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1fpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>screens.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="script.rpy-item" role="treeitem" aria-labelledby=":R1hpimplab:" aria-describedby=":R1hpimplabH1:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1hpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1hpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>script.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="work_sessions.json-item" role="treeitem" aria-labelledby=":R1jpimplab:" aria-describedby=":R1jpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1jpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1jpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>work_sessions.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="wt_core.rpy-item" role="treeitem" aria-labelledby=":R1lpimplab:" aria-describedby=":R1lpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1lpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1lpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>wt_core.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="wt_ep01.rpy-item" role="treeitem" aria-labelledby=":R1npimplab:" aria-describedby=":R1npimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1npimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1npimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>wt_ep01.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="wt_ep02.rpy-item" role="treeitem" aria-labelledby=":R1ppimplab:" aria-describedby=":R1ppimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1ppimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1ppimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>wt_ep02.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="wt_ep03.rpy-item" role="treeitem" aria-labelledby=":R1rpimplab:" aria-describedby=":R1rpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1rpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1rpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>wt_ep03.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="wt_ep04.rpy-item" role="treeitem" aria-labelledby=":R1tpimplab:" aria-describedby=":R1tpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1tpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1tpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>wt_ep04.rpy</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-ShJr0" tabindex="0" id="wt_ep05.rpy-item" role="treeitem" aria-labelledby=":R1vpimplab:" aria-describedby=":R1vpimplabH1:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer--2Rkn" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R1vpimplab:" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-f0r0b"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-4-mPv" aria-hidden="true" id=":R1vpimplabH1:"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-dRlGq" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-smZM-"><span>wt_ep05.rpy</span></span></div></div></li></ul></nav></div></div></div></div></div></div><div class="prc-PageLayout-VerticalDivider-4A4Qm prc-PageLayout-PaneVerticalDivider-1c9vy" data-variant-narrow="none" data-variant-regular="line" data-variant-wide="line" data-position="start" style="--spacing:var(--spacing-none)"><div class="prc-PageLayout-DraggableHandle-zPw82" data-dragging="false" role="slider" aria-label="Draggable pane splitter" aria-valuemin="0" aria-valuemax="0" aria-valuenow="0" aria-valuetext="Pane width 0 pixels" tabindex="0"></div></div></div></div><div class="prc-PageLayout-ContentWrapper-b-QRo CodeView-module__SplitPageLayout_Content--qxR1C" data-is-hidden-narrow="true"><div class="prc-PageLayout-Content--F7-I" data-width="full" style="--spacing:var(--spacing-none)"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-62in7e-0 cybVuK"><div class="Box-sc-62in7e-0 gSjuRy"><div class="container CodeViewHeader-module__Box--PofRM"><div class="px-3 pt-3 pb-0" id="StickyHeader"><div class="CodeViewHeader-module__Box_1--KpLzV"><div class="CodeViewHeader-module__Box_2--xzDOt"><div class="CodeViewHeader-module__Box_6--iStzT"><div class="Box-sc-62in7e-0 kfsEDb"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Box-sc-62in7e-0 eLrlvS"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Box-sc-62in7e-0 fNzIif"><li class="Box-sc-62in7e-0 iRLfgU"><a class="Link__StyledLink-sc-1syctfj-0 htWjsS prc-Link-Link-85e08" data-testid="breadcrumbs-repo-link" href="/yukihina/htl66/tree/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q" data-discover="true">htl66</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-62in7e-0 iRLfgU"><span class="Text__StyledText-sc-1klmep6-0 xsVwu prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading-sc-1vc165i-0 hJQQvf">script.rpy</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-c50BI ml-2 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":R3nb9lab:-loading-announcement" aria-labelledby=":R3b9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="Box-sc-62in7e-0 CopyToClipboardButton-module__tooltip--HDUYz prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-label="Copy path" aria-hidden="true" id=":R3b9lab:">Copy path</span></div></div><div class="react-code-view-header-element--wide"><div class="CodeViewHeader-module__Box_7--FZfkg"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button type="button" class="prc-Button-ButtonBase-c50BI Button__StyledButtonComponent-sc-vqy3e4-0 hfSsoj NavigationMenu-module__Button--SJihq" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R1ahj9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click NavigationMenu-module__IconButton--NqJ_L prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rihj9lab:-loading-announcement" aria-labelledby=":Rfihj9lab:" id=":Rihj9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":Rfihj9lab:">More file actions</span> </div></div></div><div class="react-code-view-header-element--narrow"><div class="CodeViewHeader-module__Box_7--FZfkg"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><button type="button" class="prc-Button-ButtonBase-c50BI Button__StyledButtonComponent-sc-vqy3e4-0 hfSsoj NavigationMenu-module__Button--SJihq" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":R1ahr9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI js-blob-dropdown-click NavigationMenu-module__IconButton--NqJ_L prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-describedby=":Rihr9lab:-loading-announcement" aria-labelledby=":Rfihr9lab:" id=":Rihr9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":Rfihr9lab:">More file actions</span> </div></div></div></div></div></div></div></div><div class="Box-sc-62in7e-0 jyTWxL react-code-view-bottom-padding"> <div class="BlobTopBanners-module__Box--g_bGk"></div> <!-- --> <!-- --> </div><div class="Box-sc-62in7e-0 jyTWxL"> <!-- --> <!-- --> <div class="d-flex flex-column border rounded-2 mb-3 pl-1"><div class="LatestCommit-module__Box--Fimpo"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">History</h2><a href="/yukihina/htl66/commits/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy" class="prc-Button-ButtonBase-c50BI d-none d-lg-flex LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R2mlal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="History" id="history-icon-button-tooltip" class="prc-Tooltip-Tooltip--1XZX prc-Tooltip-Tooltip--n-BOOzB tooltipped-n"><a aria-label="View commit history for this file." href="/yukihina/htl66/commits/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy" class="prc-Button-ButtonBase-c50BI LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":Rcmlal9lab:-loading-announcement history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></div><div class="Box-sc-62in7e-0 hGzGyY"><div class="Box-sc-62in7e-0 cJXRZE container"><div class="Box-sc-62in7e-0 fpyUWF react-code-size-details-banner"><div class="react-code-size-details-banner CodeSizeDetails-module__Box--QdxnQ"><div class="text-mono CodeSizeDetails-module__Box_1--_uFDs"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1--er0Uk prc-Truncate-Truncate-A9Wn6" data-inline="true" title="8.32 KB" style="--truncate-max-width:100%"><span>226 lines (185 loc) · 8.32 KB</span></div></div></div><div class="react-code-size-details-banner"><button type="button" style="--button-color:fg.default" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="Code 55% faster with GitHub Copilot" class="prc-Button-ButtonBase-c50BI Button__StyledButtonComponent-sc-vqy3e4-0 eNrdFK" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":Ripal9lab:-loading-announcement" id=":Ripal9lab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span></button></div></div><div class="Box-sc-62in7e-0 iafbuG react-blob-view-header-sticky" id="repos-sticky-header"><div class="BlobViewHeader-module__Box--pvsIA"><div class="react-blob-sticky-header"><div class="Box-sc-62in7e-0 iNRqcN"><div class="FileNameStickyHeader-module__Box_5--xBJ2J"><div class="Box-sc-62in7e-0 igwLyx"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-62in7e-0 eLrlvS"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-62in7e-0 fNzIif"><li class="Box-sc-62in7e-0 iRLfgU"><a class="Link__StyledLink-sc-1syctfj-0 htWjsS prc-Link-Link-85e08" data-testid="breadcrumbs-repo-link" href="/yukihina/htl66/tree/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q" data-discover="true">htl66</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-62in7e-0 iRLfgU"><span class="Text__StyledText-sc-1klmep6-0 iHrMHQ prc-Text-Text-0ima0" aria-hidden="true">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading-sc-1vc165i-0 cGzJbh">script.rpy</h1></div></div><button type="button" class="prc-Button-ButtonBase-c50BI Button__StyledButtonComponent-sc-vqy3e4-0 FileNameStickyHeader-module__Button--SaiiH FileNameStickyHeader-module__GoToTopButton--9lB4x" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R9cpal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Top</span></span></button></div></div></div><div class="Box-sc-62in7e-0 koZdcA BlobViewHeader-module__Box_1--PPihg"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-6CmGO" data-testid="screen-reader-heading">File metadata and controls</h2><div class="BlobViewHeader-module__Box_2--G_jCG"><ul aria-label="File view" class="prc-SegmentedControl-SegmentedControl-e7570 BlobTabButtons-module__SegmentedControl--JMGov" data-size="small"><li class="prc-SegmentedControl-Item-7Aq6h" data-selected=""><button aria-current="true" class="prc-SegmentedControl-Button-ojWXD" type="button" style="--separator-color:transparent"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Code">Code</div></span></button></li><li class="prc-SegmentedControl-Item-7Aq6h"><button aria-current="false" class="prc-SegmentedControl-Button-ojWXD" type="button" style="--separator-color:var(--borderColor-default)"><span class="prc-SegmentedControl-Content-gnQ4n segmentedControl-content"><div class="prc-SegmentedControl-Text-c5gSh segmentedControl-text" data-text="Blame">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="react-code-size-details-in-header CodeSizeDetails-module__Box--QdxnQ"><div class="text-mono CodeSizeDetails-module__Box_1--_uFDs"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1--er0Uk prc-Truncate-Truncate-A9Wn6" data-inline="true" title="8.32 KB" style="--truncate-max-width:100%"><span>226 lines (185 loc) · 8.32 KB</span></div></div></div><div class="react-code-size-details-in-header"><button type="button" style="--button-color:fg.default" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="Code 55% faster with GitHub Copilot" class="prc-Button-ButtonBase-c50BI Button__StyledButtonComponent-sc-vqy3e4-0 eNrdFK" data-loading="false" data-size="small" data-variant="invisible" aria-describedby=":R1qcpal9lab:-loading-announcement" id=":R1qcpal9lab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span></button></div></div><div class="BlobViewHeader-module__Box_3--Kvpex"><div class="react-blob-header-edit-and-raw-actions BlobViewHeader-module__Box_4--vFP89"><div class="prc-ButtonGroup-ButtonGroup-vcMeG"><div><a href="https://github.com/yukihina/htl66/raw/refs/heads/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy" data-testid="raw-button" class="prc-Button-ButtonBase-c50BI LinkButton-sc-1v6zkmg-0 iwmTUC BlobViewHeader-module__LinkButton--DMph4" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R5becpal9lab:-loading-announcement"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="text" class="prc-Button-Label-pTQ3x">Raw</span></span></a></div><div><button data-component="IconButton" type="button" data-testid="copy-raw-button" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R6pbecpal9lab:-loading-announcement" aria-labelledby=":Rpbecpal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":Rpbecpal9lab:">Copy raw file</span></div><div><button data-component="IconButton" type="button" data-testid="download-raw-button" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 gXjFlG prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R1tbecpal9lab:-loading-announcement" aria-labelledby=":Rdbecpal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="n" aria-hidden="true" id=":Rdbecpal9lab:">Download raw file</span></div></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-85e08" href="https://github.dev/" target="_blank"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="prc-ButtonGroup-ButtonGroup-vcMeG"><div><a data-component="IconButton" type="button" data-testid="edit-button" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 gRAczH BlobViewHeader-module__IconButton_1--MzNlL prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":R1mjecpal9lab:-loading-announcement" aria-labelledby=":R6jecpal9lab:" href="/yukihina/htl66/edit/claude/implement-auto-progression-rates-014rTUSkBwksKqqVA41Rxc4Q/script.rpy" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R6jecpal9lab:">Edit this file</span></div><div><button data-component="IconButton" type="button" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-describedby=":Rajecpal9lab:-loading-announcement" aria-labelledby=":R7qjecpal9lab:" id=":Rajecpal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R7qjecpal9lab:">More edit options</span></div></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" aria-controls="symbols-pane" data-testid="symbols-button" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 BlobViewHeader-module__IconButton_2--KDy6i prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby="symbols-button-loading-announcement" aria-labelledby=":R3ucpal9lab:" id="symbols-button"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":R3ucpal9lab:">Open symbols panel</span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI IconButton__StyledIconButton-sc-i53dt6-0 js-blob-dropdown-click BlobViewHeader-module__IconButton--uO1fA prc-Button-IconButton-szpyj" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-describedby=":Rkucpal9lab:-loading-announcement" aria-labelledby=":Rfkucpal9lab:" id=":Rkucpal9lab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-cYMVY" data-direction="nw" aria-hidden="true" id=":Rfkucpal9lab:">Edit and raw actions</span></div></div></div></div><div></div></div><div class="Box-sc-62in7e-0 dIDnLY"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-62in7e-0 hhuNfn"><div class="Box-sc-62in7e-0 hNuvaP"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-62in7e-0 kBkfpQ"><div class="Box-sc-62in7e-0 lnfLer"><div class="Box-sc-62in7e-0 djZnHX react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="4" data-paste-markdown-skip="true" data-hpc="true"><div class="react-line-numbers-no-virtualization" style="pointer-events:auto;position:relative;z-index:2"><div class="react-no-virtualization-wrapper-lines-ssr"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right:16px">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right:16px">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right:16px">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right:16px">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right:16px">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right:16px">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right:16px">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right:16px">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right:16px">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right:16px">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right:16px">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right:16px">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right:16px">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right:16px">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right:16px">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right:16px">16</div><div data-line-number="17" class="react-line-number react-code-text" style="padding-right:16px">17</div><div data-line-number="18" class="react-line-number react-code-text" style="padding-right:16px">18</div><div data-line-number="19" class="react-line-number react-code-text" style="padding-right:16px">19</div><div data-line-number="20" class="react-line-number react-code-text" style="padding-right:16px">20</div><div data-line-number="21" class="react-line-number react-code-text" style="padding-right:16px">21</div><div data-line-number="22" class="react-line-number react-code-text" style="padding-right:16px">22</div><div data-line-number="23" class="react-line-number react-code-text" style="padding-right:16px">23</div><div data-line-number="24" class="react-line-number react-code-text" style="padding-right:16px">24</div><div data-line-number="25" class="react-line-number react-code-text" style="padding-right:16px">25</div><div data-line-number="26" class="react-line-number react-code-text" style="padding-right:16px">26</div><div data-line-number="27" class="react-line-number react-code-text" style="padding-right:16px">27</div><div data-line-number="28" class="react-line-number react-code-text" style="padding-right:16px">28</div><div data-line-number="29" class="react-line-number react-code-text" style="padding-right:16px">29</div><div data-line-number="30" class="react-line-number react-code-text" style="padding-right:16px">30</div><div data-line-number="31" class="react-line-number react-code-text" style="padding-right:16px">31</div><div data-line-number="32" class="react-line-number react-code-text" style="padding-right:16px">32</div><div data-line-number="33" class="react-line-number react-code-text" style="padding-right:16px">33</div><div data-line-number="34" class="react-line-number react-code-text" style="padding-right:16px">34</div><div data-line-number="35" class="react-line-number react-code-text" style="padding-right:16px">35</div><div data-line-number="36" class="react-line-number react-code-text" style="padding-right:16px">36</div><div data-line-number="37" class="react-line-number react-code-text" style="padding-right:16px">37</div><div data-line-number="38" class="react-line-number react-code-text" style="padding-right:16px">38</div><div data-line-number="39" class="react-line-number react-code-text" style="padding-right:16px">39</div><div data-line-number="40" class="react-line-number react-code-text" style="padding-right:16px">40</div><div data-line-number="41" class="react-line-number react-code-text" style="padding-right:16px">41</div><div data-line-number="42" class="react-line-number react-code-text" style="padding-right:16px">42</div><div data-line-number="43" class="react-line-number react-code-text" style="padding-right:16px">43</div><div data-line-number="44" class="react-line-number react-code-text" style="padding-right:16px">44</div><div data-line-number="45" class="react-line-number react-code-text" style="padding-right:16px">45</div><div data-line-number="46" class="react-line-number react-code-text" style="padding-right:16px">46</div><div data-line-number="47" class="react-line-number react-code-text" style="padding-right:16px">47</div><div data-line-number="48" class="react-line-number react-code-text" style="padding-right:16px">48</div><div data-line-number="49" class="react-line-number react-code-text" style="padding-right:16px">49</div><div data-line-number="50" class="react-line-number react-code-text" style="padding-right:16px">50</div><div data-line-number="51" class="react-line-number react-code-text" style="padding-right:16px">51</div><div data-line-number="52" class="react-line-number react-code-text" style="padding-right:16px">52</div><div data-line-number="53" class="react-line-number react-code-text" style="padding-right:16px">53</div><div data-line-number="54" class="react-line-number react-code-text" style="padding-right:16px">54</div><div data-line-number="55" class="react-line-number react-code-text" style="padding-right:16px">55</div><div data-line-number="56" class="react-line-number react-code-text" style="padding-right:16px">56</div><div data-line-number="57" class="react-line-number react-code-text" style="padding-right:16px">57</div><div data-line-number="58" class="react-line-number react-code-text" style="padding-right:16px">58</div><div data-line-number="59" class="react-line-number react-code-text" style="padding-right:16px">59</div><div data-line-number="60" class="react-line-number react-code-text" style="padding-right:16px">60</div></div><div class="react-no-virtualization-wrapper-lines-ssr"><div data-line-number="61" class="react-line-number react-code-text" style="padding-right:16px">61</div><div data-line-number="62" class="react-line-number react-code-text" style="padding-right:16px">62</div><div data-line-number="63" class="react-line-number react-code-text" style="padding-right:16px">63</div><div data-line-number="64" class="react-line-number react-code-text" style="padding-right:16px">64</div><div data-line-number="65" class="react-line-number react-code-text" style="padding-right:16px">65</div><div data-line-number="66" class="react-line-number react-code-text" style="padding-right:16px">66</div><div data-line-number="67" class="react-line-number react-code-text" style="padding-right:16px">67</div><div data-line-number="68" class="react-line-number react-code-text" style="padding-right:16px">68</div><div data-line-number="69" class="react-line-number react-code-text" style="padding-right:16px">69</div><div data-line-number="70" class="react-line-number react-code-text" style="padding-right:16px">70</div><div data-line-number="71" class="react-line-number react-code-text" style="padding-right:16px">71</div><div data-line-number="72" class="react-line-number react-code-text" style="padding-right:16px">72</div><div data-line-number="73" class="react-line-number react-code-text" style="padding-right:16px">73</div><div data-line-number="74" class="react-line-number react-code-text" style="padding-right:16px">74</div><div data-line-number="75" class="react-line-number react-code-text" style="padding-right:16px">75</div><div data-line-number="76" class="react-line-number react-code-text" style="padding-right:16px">76</div><div data-line-number="77" class="react-line-number react-code-text" style="padding-right:16px">77</div><div data-line-number="78" class="react-line-number react-code-text" style="padding-right:16px">78</div><div data-line-number="79" class="react-line-number react-code-text" style="padding-right:16px">79</div><div data-line-number="80" class="react-line-number react-code-text" style="padding-right:16px">80</div><div data-line-number="81" class="react-line-number react-code-text" style="padding-right:16px">81</div><div data-line-number="82" class="react-line-number react-code-text" style="padding-right:16px">82</div><div data-line-number="83" class="react-line-number react-code-text" style="padding-right:16px">83</div><div data-line-number="84" class="react-line-number react-code-text" style="padding-right:16px">84</div><div data-line-number="85" class="react-line-number react-code-text" style="padding-right:16px">85</div><div data-line-number="86" class="react-line-number react-code-text" style="padding-right:16px">86</div><div data-line-number="87" class="react-line-number react-code-text" style="padding-right:16px">87</div><div data-line-number="88" class="react-line-number react-code-text" style="padding-right:16px">88</div><div data-line-number="89" class="react-line-number react-code-text" style="padding-right:16px">89</div><div data-line-number="90" class="react-line-number react-code-text" style="padding-right:16px">90</div><div data-line-number="91" class="react-line-number react-code-text" style="padding-right:16px">91</div><div data-line-number="92" class="react-line-number react-code-text" style="padding-right:16px">92</div><div data-line-number="93" class="react-line-number react-code-text" style="padding-right:16px">93</div><div data-line-number="94" class="react-line-number react-code-text" style="padding-right:16px">94</div><div data-line-number="95" class="react-line-number react-code-text" style="padding-right:16px">95</div><div data-line-number="96" class="react-line-number react-code-text" style="padding-right:16px">96</div><div data-line-number="97" class="react-line-number react-code-text" style="padding-right:16px">97</div><div data-line-number="98" class="react-line-number react-code-text" style="padding-right:16px">98</div><div data-line-number="99" class="react-line-number react-code-text" style="padding-right:16px">99</div><div data-line-number="100" class="react-line-number react-code-text" style="padding-right:16px">100</div><div data-line-number="101" class="react-line-number react-code-text" style="padding-right:16px">101</div><div data-line-number="102" class="react-line-number react-code-text" style="padding-right:16px">102</div><div data-line-number="103" class="react-line-number react-code-text" style="padding-right:16px">103</div><div data-line-number="104" class="react-line-number react-code-text" style="padding-right:16px">104</div><div data-line-number="105" class="react-line-number react-code-text" style="padding-right:16px">105</div><div data-line-number="106" class="react-line-number react-code-text" style="padding-right:16px">106</div><div data-line-number="107" class="react-line-number react-code-text" style="padding-right:16px">107</div><div data-line-number="108" class="react-line-number react-code-text" style="padding-right:16px">108</div><div data-line-number="109" class="react-line-number react-code-text" style="padding-right:16px">109</div><div data-line-number="110" class="react-line-number react-code-text" style="padding-right:16px">110</div><div data-line-number="111" class="react-line-number react-code-text" style="padding-right:16px">111</div><div data-line-number="112" class="react-line-number react-code-text" style="padding-right:16px">112</div><div data-line-number="113" class="react-line-number react-code-text" style="padding-right:16px">113</div><div data-line-number="114" class="react-line-number react-code-text" style="padding-right:16px">114</div><div data-line-number="115" class="react-line-number react-code-text" style="padding-right:16px">115</div><div data-line-number="116" class="react-line-number react-code-text" style="padding-right:16px">116</div><div data-line-number="117" class="react-line-number react-code-text" style="padding-right:16px">117</div><div data-line-number="118" class="react-line-number react-code-text" style="padding-right:16px">118</div><div data-line-number="119" class="react-line-number react-code-text" style="padding-right:16px">119</div><div data-line-number="120" class="react-line-number react-code-text" style="padding-right:16px">120</div></div><div class="react-no-virtualization-wrapper-lines-ssr"><div data-line-number="121" class="react-line-number react-code-text" style="padding-right:16px">121</div><div data-line-number="122" class="react-line-number react-code-text" style="padding-right:16px">122</div><div data-line-number="123" class="react-line-number react-code-text" style="padding-right:16px">123</div><div data-line-number="124" class="react-line-number react-code-text" style="padding-right:16px">124</div><div data-line-number="125" class="react-line-number react-code-text" style="padding-right:16px">125</div><div data-line-number="126" class="react-line-number react-code-text" style="padding-right:16px">126</div><div data-line-number="127" class="react-line-number react-code-text" style="padding-right:16px">127</div><div data-line-number="128" class="react-line-number react-code-text" style="padding-right:16px">128</div><div data-line-number="129" class="react-line-number react-code-text" style="padding-right:16px">129</div><div data-line-number="130" class="react-line-number react-code-text" style="padding-right:16px">130</div><div data-line-number="131" class="react-line-number react-code-text" style="padding-right:16px">131</div><div data-line-number="132" class="react-line-number react-code-text" style="padding-right:16px">132</div><div data-line-number="133" class="react-line-number react-code-text" style="padding-right:16px">133</div><div data-line-number="134" class="react-line-number react-code-text" style="padding-right:16px">134</div><div data-line-number="135" class="react-line-number react-code-text" style="padding-right:16px">135</div><div data-line-number="136" class="react-line-number react-code-text" style="padding-right:16px">136</div><div data-line-number="137" class="react-line-number react-code-text" style="padding-right:16px">137</div><div data-line-number="138" class="react-line-number react-code-text" style="padding-right:16px">138</div><div data-line-number="139" class="react-line-number react-code-text" style="padding-right:16px">139</div><div data-line-number="140" class="react-line-number react-code-text" style="padding-right:16px">140</div><div data-line-number="141" class="react-line-number react-code-text" style="padding-right:16px">141</div><div data-line-number="142" class="react-line-number react-code-text" style="padding-right:16px">142</div><div data-line-number="143" class="react-line-number react-code-text" style="padding-right:16px">143</div><div data-line-number="144" class="react-line-number react-code-text" style="padding-right:16px">144</div><div data-line-number="145" class="react-line-number react-code-text" style="padding-right:16px">145</div><div data-line-number="146" class="react-line-number react-code-text" style="padding-right:16px">146</div><div data-line-number="147" class="react-line-number react-code-text" style="padding-right:16px">147</div><div data-line-number="148" class="react-line-number react-code-text" style="padding-right:16px">148</div><div data-line-number="149" class="react-line-number react-code-text" style="padding-right:16px">149</div><div data-line-number="150" class="react-line-number react-code-text" style="padding-right:16px">150</div><div data-line-number="151" class="react-line-number react-code-text" style="padding-right:16px">151</div><div data-line-number="152" class="react-line-number react-code-text" style="padding-right:16px">152</div><div data-line-number="153" class="react-line-number react-code-text" style="padding-right:16px">153</div><div data-line-number="154" class="react-line-number react-code-text" style="padding-right:16px">154</div><div data-line-number="155" class="react-line-number react-code-text" style="padding-right:16px">155</div><div data-line-number="156" class="react-line-number react-code-text" style="padding-right:16px">156</div><div data-line-number="157" class="react-line-number react-code-text" style="padding-right:16px">157</div><div data-line-number="158" class="react-line-number react-code-text" style="padding-right:16px">158</div><div data-line-number="159" class="react-line-number react-code-text" style="padding-right:16px">159</div><div data-line-number="160" class="react-line-number react-code-text" style="padding-right:16px">160</div><div data-line-number="161" class="react-line-number react-code-text" style="padding-right:16px">161</div><div data-line-number="162" class="react-line-number react-code-text" style="padding-right:16px">162</div><div data-line-number="163" class="react-line-number react-code-text" style="padding-right:16px">163</div><div data-line-number="164" class="react-line-number react-code-text" style="padding-right:16px">164</div><div data-line-number="165" class="react-line-number react-code-text" style="padding-right:16px">165</div><div data-line-number="166" class="react-line-number react-code-text" style="padding-right:16px">166</div><div data-line-number="167" class="react-line-number react-code-text" style="padding-right:16px">167</div><div data-line-number="168" class="react-line-number react-code-text" style="padding-right:16px">168</div><div data-line-number="169" class="react-line-number react-code-text" style="padding-right:16px">169</div><div data-line-number="170" class="react-line-number react-code-text" style="padding-right:16px">170</div><div data-line-number="171" class="react-line-number react-code-text" style="padding-right:16px">171</div><div data-line-number="172" class="react-line-number react-code-text" style="padding-right:16px">172</div><div data-line-number="173" class="react-line-number react-code-text" style="padding-right:16px">173</div><div data-line-number="174" class="react-line-number react-code-text" style="padding-right:16px">174</div><div data-line-number="175" class="react-line-number react-code-text" style="padding-right:16px">175</div><div data-line-number="176" class="react-line-number react-code-text" style="padding-right:16px">176</div><div data-line-number="177" class="react-line-number react-code-text" style="padding-right:16px">177</div><div data-line-number="178" class="react-line-number react-code-text" style="padding-right:16px">178</div><div data-line-number="179" class="react-line-number react-code-text" style="padding-right:16px">179</div><div data-line-number="180" class="react-line-number react-code-text" style="padding-right:16px">180</div></div><div class="react-no-virtualization-wrapper-lines-ssr"><div data-line-number="181" class="react-line-number react-code-text" style="padding-right:16px">181</div><div data-line-number="182" class="react-line-number react-code-text" style="padding-right:16px">182</div><div data-line-number="183" class="react-line-number react-code-text" style="padding-right:16px">183</div><div data-line-number="184" class="react-line-number react-code-text" style="padding-right:16px">184</div><div data-line-number="185" class="react-line-number react-code-text" style="padding-right:16px">185</div><div data-line-number="186" class="react-line-number react-code-text" style="padding-right:16px">186</div><div data-line-number="187" class="react-line-number react-code-text" style="padding-right:16px">187</div><div data-line-number="188" class="react-line-number react-code-text" style="padding-right:16px">188</div><div data-line-number="189" class="react-line-number react-code-text" style="padding-right:16px">189</div><div data-line-number="190" class="react-line-number react-code-text" style="padding-right:16px">190</div><div data-line-number="191" class="react-line-number react-code-text" style="padding-right:16px">191</div><div data-line-number="192" class="react-line-number react-code-text" style="padding-right:16px">192</div><div data-line-number="193" class="react-line-number react-code-text" style="padding-right:16px">193</div><div data-line-number="194" class="react-line-number react-code-text" style="padding-right:16px">194</div><div data-line-number="195" class="react-line-number react-code-text" style="padding-right:16px">195</div><div data-line-number="196" class="react-line-number react-code-text" style="padding-right:16px">196</div><div data-line-number="197" class="react-line-number react-code-text" style="padding-right:16px">197</div><div data-line-number="198" class="react-line-number react-code-text" style="padding-right:16px">198</div><div data-line-number="199" class="react-line-number react-code-text" style="padding-right:16px">199</div><div data-line-number="200" class="react-line-number react-code-text" style="padding-right:16px">200</div><div data-line-number="201" class="react-line-number react-code-text" style="padding-right:16px">201</div><div data-line-number="202" class="react-line-number react-code-text" style="padding-right:16px">202</div><div data-line-number="203" class="react-line-number react-code-text" style="padding-right:16px">203</div><div data-line-number="204" class="react-line-number react-code-text" style="padding-right:16px">204</div><div data-line-number="205" class="react-line-number react-code-text" style="padding-right:16px">205</div><div data-line-number="206" class="react-line-number react-code-text" style="padding-right:16px">206</div><div data-line-number="207" class="react-line-number react-code-text" style="padding-right:16px">207</div><div data-line-number="208" class="react-line-number react-code-text" style="padding-right:16px">208</div><div data-line-number="209" class="react-line-number react-code-text" style="padding-right:16px">209</div><div data-line-number="210" class="react-line-number react-code-text" style="padding-right:16px">210</div><div data-line-number="211" class="react-line-number react-code-text" style="padding-right:16px">211</div><div data-line-number="212" class="react-line-number react-code-text" style="padding-right:16px">212</div><div data-line-number="213" class="react-line-number react-code-text" style="padding-right:16px">213</div><div data-line-number="214" class="react-line-number react-code-text" style="padding-right:16px">214</div><div data-line-number="215" class="react-line-number react-code-text" style="padding-right:16px">215</div><div data-line-number="216" class="react-line-number react-code-text" style="padding-right:16px">216</div><div data-line-number="217" class="react-line-number react-code-text" style="padding-right:16px">217</div><div data-line-number="218" class="react-line-number react-code-text" style="padding-right:16px">218</div><div data-line-number="219" class="react-line-number react-code-text" style="padding-right:16px">219</div><div data-line-number="220" class="react-line-number react-code-text" style="padding-right:16px">220</div><div data-line-number="221" class="react-line-number react-code-text" style="padding-right:16px">221</div><div data-line-number="222" class="react-line-number react-code-text" style="padding-right:16px">222</div><div data-line-number="223" class="react-line-number react-code-text" style="padding-right:16px">223</div><div data-line-number="224" class="react-line-number react-code-text" style="padding-right:16px">224</div><div data-line-number="225" class="react-line-number react-code-text" style="padding-right:16px">225</div><div data-line-number="226" class="react-line-number react-code-text" style="padding-right:16px">226</div></div></div><div class="react-code-lines"><div><div id="LC1" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">init</span>:</div>
<div id="LC2" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.effectsOn <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC3" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">define</span> _scene_show_hide_transition <span class="pl-k">=</span> Dissolve(<span class="pl-c1">0.35</span>)</div>
<div id="LC4" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> mc_name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></div>
<div id="LC5" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> walkthrough_enabled <span class="pl-k">=</span> <span class="pl-c1">False</span></div>
<div id="LC6" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.walkthrough_all <span class="pl-k">=</span> <span class="pl-c1">False</span></div>
<div id="LC7" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.walkthrough_li <span class="pl-k">=</span> <span class="pl-c1">set</span>()</div>
<div id="LC8" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.disclaimer <span class="pl-k">=</span> <span class="pl-c1">False</span></div>
<div id="LC9" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> htl_episodes <span class="pl-k">=</span> <span class="pl-c1">6.1</span></div>
<div id="LC10" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> rm <span class="pl-k">=</span> RM()</div>
<div id="LC11" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> ss <span class="pl-k">=</span> SexStats()</div>
<div id="LC12" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC13" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"><span class="pl-c">#</span> Persistent path lock variables for Milestone Decision System</span></div>
<div id="LC14" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"><span class="pl-c">#</span> Values: &quot;love&quot;, &quot;corruption&quot;, &quot;neutral&quot;, or None (unlocked)</span></div>
<div id="LC15" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.amber_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC16" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.nanami_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC17" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.elizabeth_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC18" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.isabella_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC19" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.kanae_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC20" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.arlette_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC21" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.antonella_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC22" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.madison_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC23" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">default</span> persistent.paz_path <span class="pl-k">=</span> <span class="pl-c1">None</span></div>
<div id="LC24" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC25" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC26" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span>###############################################################################</span></div>
<div id="LC27" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span># MILESTONE DECISION SYSTEM - Episode 6+ Path Locking</span></div>
<div id="LC28" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span>###############################################################################</span></div>
<div id="LC29" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span># These counters track significant path-defining choices for each character</span></div>
<div id="LC30" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span># When a counter reaches a threshold (typically 3), the character&#39;s path locks</span></div>
<div id="LC31" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC32" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Amber milestone counters</span></div>
<div id="LC33" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> amber_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC34" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> amber_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC35" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC36" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Nanami milestone counters</span></div>
<div id="LC37" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> nanami_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC38" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> nanami_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC39" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC40" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Elizabeth milestone counters</span></div>
<div id="LC41" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> elizabeth_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC42" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> elizabeth_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC43" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC44" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Isabella milestone counters</span></div>
<div id="LC45" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> isabella_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC46" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> isabella_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC47" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC48" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Kanae milestone counters</span></div>
<div id="LC49" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> kanae_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC50" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> kanae_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC51" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC52" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Arlette milestone counters</span></div>
<div id="LC53" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> arlette_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC54" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> arlette_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC55" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC56" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Antonella milestone counters</span></div>
<div id="LC57" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> antonella_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC58" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> antonella_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC59" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC60" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Madison milestone counters</span></div>
<div id="LC61" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> madison_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC62" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> madison_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC63" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC64" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span> Paz milestone counters</span></div>
<div id="LC65" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> paz_love_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC66" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> paz_cor_choices <span class="pl-k">=</span> <span class="pl-c1">0</span></div>
<div id="LC67" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC68" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC69" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span>###############################################################################</span></div>
<div id="LC70" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span># SAVE SYSTEM VERSION - For Migration Tracking</span></div>
<div id="LC71" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span>###############################################################################</span></div>
<div id="LC72" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span># Version 1: Original system without automatic progression rates (default for old saves)</span></div>
<div id="LC73" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-c"><span class="pl-c">#</span># Version 2: New system with automatic character progression rate multipliers</span></div>
<div id="LC74" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">default</span> save_system_version <span class="pl-k">=</span> <span class="pl-c1">1</span></div>
<div id="LC75" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC76" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC77" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">init</span> <span class="pl-k">python</span>:</div>
<div id="LC78" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">def</span> <span class="pl-en">show_walkthrough</span>(<span class="pl-smi">key</span>):</div>
<div id="LC79" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">if</span> walkthrough_enabled <span class="pl-k">and</span> renpy.loadable(<span class="pl-s"><span class="pl-pds">&quot;</span>wt_core.rpyc<span class="pl-pds">&quot;</span></span>):</div>
<div id="LC80" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">if</span> walkthrough_all:</div>
<div id="LC81" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                messages <span class="pl-k">=</span> []</div>
<div id="LC82" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                <span class="pl-k">for</span> option <span class="pl-k">in</span> walkthrough_data.get(<span class="pl-k">key</span>, {}):</div>
<div id="LC83" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                    <span class="pl-k">if</span> option <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>all<span class="pl-pds">&quot;</span></span>:</div>
<div id="LC84" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                        messages.append(walkthrough_data[<span class="pl-k">key</span>][option])</div>
<div id="LC85" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                message <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span>.join(messages)</div>
<div id="LC86" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">else</span>:</div>
<div id="LC87" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                message <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></div>
<div id="LC88" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                <span class="pl-k">for</span> option <span class="pl-k">in</span> walkthrough_li:</div>
<div id="LC89" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                    <span class="pl-k">if</span> option <span class="pl-k">in</span> walkthrough_data.get(<span class="pl-k">key</span>, {}):</div>
<div id="LC90" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                        message <span class="pl-k">+=</span> walkthrough_data[<span class="pl-k">key</span>][option] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></div>
<div id="LC91" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC92" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">if</span> message:</div>
<div id="LC93" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                renpy.show_screen(<span class="pl-s"><span class="pl-pds">&quot;</span>walkthrough_screen<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">message</span><span class="pl-k">=</span>message)</div>
<div id="LC94" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC95" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">def</span> <span class="pl-en">update_htl_episodes</span>():</div>
<div id="LC96" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">global</span> htl_episodes</div>
<div id="LC97" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">if</span> <span class="pl-k">not</span> htl_episodes <span class="pl-k">==</span> <span class="pl-c1">6.1</span>:</div>
<div id="LC98" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            htl_episodes <span class="pl-k">=</span> <span class="pl-c1">6.1</span></div>
<div id="LC99" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC100" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">label</span> <span class="pl-en">splashscreen</span>:</div>
<div id="LC101" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">scene</span> black</div>
<div id="LC102" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> nl_bg <span class="pl-k">with</span> clouds_inverse_simple</div>
<div id="LC103" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> renpy.pause(<span class="pl-c1">0.1</span>, <span class="pl-smi">hard</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</div>
<div id="LC104" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> setChannelVolume(<span class="pl-smi">channel</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">subchannel</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-smi">volume</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</div>
<div id="LC105" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> playAudio(sfx_logo_brush, <span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">5</span>, <span class="pl-c1">False</span>, <span class="pl-smi">fadein</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">fadeout</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</div>
<div id="LC106" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> nl_lo:</div>
<div id="LC107" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-e">yalign</span> <span class="pl-c1">0.30</span></div>
<div id="LC108" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-e">xalign</span> <span class="pl-c1">0.5</span></div>
<div id="LC109" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">with</span> horicolor_simple</div>
<div id="LC110" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> setChannelVolume(<span class="pl-smi">channel</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">subchannel</span><span class="pl-k">=</span><span class="pl-c1">8</span>, <span class="pl-smi">volume</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</div>
<div id="LC111" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> playAudio(sfx_logo, <span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">8</span>, <span class="pl-c1">False</span>, <span class="pl-smi">fadein</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">fadeout</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</div>
<div id="LC112" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> nl_qo <span class="pl-k">at</span> bounce <span class="pl-k">with</span> bubbles_simple</div>
<div id="LC113" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> nl_ga <span class="pl-k">at</span> neon_flicker, concentrate, sway <span class="pl-k">with</span> bubbles_simple</div>
<div id="LC114" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> nl_jp <span class="pl-k">at</span> dizzyness <span class="pl-k">with</span> cwside_simple</div>
<div id="LC115" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> setChannelVolume(<span class="pl-smi">channel</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">subchannel</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-smi">volume</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</div>
<div id="LC116" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> playAudio(sfx_logo_jp, <span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">2</span>, <span class="pl-c1">False</span>, <span class="pl-smi">fadein</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-smi">fadeout</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</div>
<div id="LC117" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> renpy.pause(<span class="pl-c1">3</span>, <span class="pl-smi">hard</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</div>
<div id="LC118" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">scene</span> black <span class="pl-k">with</span> clouds_simple</div>
<div id="LC119" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> stopAllSubchannels(<span class="pl-smi">channel</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>sfx<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">fadeout</span><span class="pl-k">=</span><span class="pl-c1">0.3</span>)</div>
<div id="LC120" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> renpy.pause(<span class="pl-c1">0.3</span>, <span class="pl-smi">hard</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</div>
<div id="LC121" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> resetAllVolumes()</div>
<div id="LC122" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">return</span></div>
<div id="LC123" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC124" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC125" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">label</span> <span class="pl-en">get_player_name</span>:</div>
<div id="LC126" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"><span class="pl-c">#</span> Asking for the player&#39;s name</span></div>
<div id="LC127" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> mc_name <span class="pl-k">=</span> renpy.input(<span class="pl-s"><span class="pl-pds">&quot;</span>What is your name?<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chris<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">length</span><span class="pl-k">=</span><span class="pl-c1">20</span>).strip()</div>
<div id="LC128" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> mc_name <span class="pl-k">=</span> mc_name <span class="pl-k">if</span> mc_name <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Chris<span class="pl-pds">&quot;</span></span></div>
<div id="LC129" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    </div>
<div id="LC130" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">return</span></div>
<div id="LC131" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC132" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC133" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC134" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">label</span> <span class="pl-en">start</span>:</div>
<div id="LC135" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> update_htl_episodes()</div>
<div id="LC136" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> save_system_version <span class="pl-k">=</span> <span class="pl-c1">2</span>  <span class="pl-c"><span class="pl-c">#</span> New games start with version 2 (automatic progression rates)</span></div>
<div id="LC137" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">stop</span> <span class="pl-k">music</span> fadeout <span class="pl-c1">0.5</span></div>
<div id="LC138" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">if</span> <span class="pl-k">not</span> persistent.disclaimer:</div>
<div id="LC139" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">$</span> persistent.disclaimer <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC140" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">call</span> <span class="pl-k">screen</span> confirm_first_time(<span class="pl-smi">message</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>This R+ rated game contains explicit sexual content, strong language, graphic violence, and adult themes. All characters are fictional and 18+. Player discretion is advised.<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">yes_action</span><span class="pl-k">=</span>Return())</div>
<div id="LC141" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">else</span>:</div>
<div id="LC142" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">pass</span></div>
<div id="LC143" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">scene</span> black <span class="pl-k">with</span> smoke</div>
<div id="LC144" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">pause</span> <span class="pl-c1">0.5</span></div>
<div id="LC145" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> playAudio(sfx_hospital_hall, <span class="pl-s"><span class="pl-pds">&quot;</span>amb<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1</span>, <span class="pl-c1">True</span>, <span class="pl-c1">1</span>, <span class="pl-c1">0</span>)</div>
<div id="LC146" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">call</span> showNoise(<span class="pl-c1">0.1</span>, <span class="pl-c1">0.15</span>, <span class="pl-smi">transition</span><span class="pl-k">=</span>dissolve)</div>
<div id="LC147" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> namechg01 <span class="pl-k">with</span> bubbles</div>
<div id="LC148" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>Nurse<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>Good morning!<span class="pl-pds">&quot;</span></span></div>
<div id="LC149" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>Nurse<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>I hope you&#39;re feeling better today. We&#39;ve got most of the boring paperwork out of the way, thanks to that gorgeous companion of yours.<span class="pl-pds">&quot;</span></span></div>
<div id="LC150" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>Nurse<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>We just need you to confirm your name for our records. Think you can manage that for me?<span class="pl-pds">&quot;</span></span></div>
<div id="LC151" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>You<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>Sure...<span class="pl-pds">&quot;</span></span></div>
<div id="LC152" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> show_custom_notification(<span class="pl-s"><span class="pl-pds">&quot;</span>start_tip<span class="pl-pds">&quot;</span></span>)</div>
<div id="LC153" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> namechg02</div>
<div id="LC154" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>Nurse<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>I must say, your companion has been incredibly attentive in filling out your information.<span class="pl-pds">&quot;</span></span></div>
<div id="LC155" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>Nurse<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>It&#39;s not often we see such dedication around here.<span class="pl-pds">&quot;</span></span></div>
<div id="LC156" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>Girl<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>Oh, it&#39;s the least I could do for him.<span class="pl-pds">&quot;</span></span></div>
<div id="LC157" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>You<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>I really appreciate it, thank you both.<span class="pl-pds">&quot;</span></span></div>
<div id="LC158" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">show</span> namechg03 <span class="pl-k">with</span> smoke</div>
<div id="LC159" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-s"><span class="pl-pds">&quot;</span>You<span class="pl-pds">&quot;</span></span> <span class="pl-s"><span class="pl-pds">&quot;</span>My name... that&#39;s all that&#39;s left, huh? Everything else has been... handled.<span class="pl-pds">&quot;</span></span></div>
<div id="LC160" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">call</span> get_player_name</div>
<div id="LC161" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    mc_t <span class="pl-s"><span class="pl-pds">&quot;</span>Alright. It&#39;s <span class="pl-c1">[mc_name]</span> then.<span class="pl-pds">&quot;</span></span></div>
<div id="LC162" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">scene</span> black <span class="pl-k">with</span> watercolor</div>
<div id="LC163" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> stopAllSubchannels(<span class="pl-smi">channel</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>amb<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">fadeout</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</div>
<div id="LC164" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">pause</span> <span class="pl-c1">1</span></div>
<div id="LC165" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">call</span> hideNoise(<span class="pl-smi">transition</span><span class="pl-k">=</span>dissolve)</div>
<div id="LC166" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">jump</span> ep01_title</div>
<div id="LC167" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">return</span></div>
<div id="LC168" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC169" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">label</span> <span class="pl-en">after_load</span>:</div>
<div id="LC170" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">call</span> hideNoise(<span class="pl-smi">transition</span><span class="pl-k">=</span>dissolve)</div>
<div id="LC171" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">$</span> update_htl_episodes()</div>
<div id="LC172" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC173" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">python</span>:</div>
<div id="LC174" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">try</span>:</div>
<div id="LC175" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC176" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">global</span> patched, patch_activated</div>
<div id="LC177" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            </div>
<div id="LC178" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC179" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">if</span> renpy.persistent.patch_applied:</div>
<div id="LC180" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                patch_activated <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC181" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                patched <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC182" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC183" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">elif</span> renpy.loadable(<span class="pl-s"><span class="pl-pds">&quot;</span>patch.rpyc<span class="pl-pds">&quot;</span></span>):</div>
<div id="LC184" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                patch_activated <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC185" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                patched <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC186" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                renpy.persistent.patch_applied <span class="pl-k">=</span> <span class="pl-c1">True</span></div>
<div id="LC187" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            </div>
<div id="LC188" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">if</span> patched:</div>
<div id="LC189" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                characters <span class="pl-k">=</span> define_characters(<span class="pl-c1">True</span>)</div>
<div id="LC190" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                relationships <span class="pl-k">=</span> define_relationships(<span class="pl-c1">True</span>)</div>
<div id="LC191" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                <span class="pl-c1">globals</span>().update(characters)</div>
<div id="LC192" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                <span class="pl-c1">globals</span>().update(relationships)</div>
<div id="LC193" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">except</span>:</div>
<div id="LC194" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">pass</span></div>
<div id="LC195" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC196" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"><span class="pl-c">#</span> Migrate old saves to new emotional lock system</span></div>
<div id="LC197" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">python</span>:</div>
<div id="LC198" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c"><span class="pl-c">#</span> Migrate RM class to include emotionally_locked field</span></div>
<div id="LC199" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">if</span> <span class="pl-c1">hasattr</span>(store, <span class="pl-s"><span class="pl-pds">&#39;</span>rm<span class="pl-pds">&#39;</span></span>):</div>
<div id="LC200" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            rm.migrate_old_saves()</div>
<div id="LC201" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC202" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c"><span class="pl-c">#</span> Check and apply emotional locks for characters with 3 strikes</span></div>
<div id="LC203" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">for</span> char <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>amber<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>nanami<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>elizabeth<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>isabella<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>kanae<span class="pl-pds">&quot;</span></span>,</div>
<div id="LC204" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                     <span class="pl-s"><span class="pl-pds">&quot;</span>arlette<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>antonella<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>madison<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>paz<span class="pl-pds">&quot;</span></span>]:</div>
<div id="LC205" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            strikes <span class="pl-k">=</span> ss.get(char, <span class="pl-s"><span class="pl-pds">&quot;</span>strike<span class="pl-pds">&quot;</span></span>)</div>
<div id="LC206" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">            <span class="pl-k">if</span> strikes <span class="pl-k">&gt;=</span> <span class="pl-c1">3</span>:</div>
<div id="LC207" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">                rm.check_emotional_lock(char)</div>
<div id="LC208" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC209" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"><span class="pl-c">#</span> Migrate old saves to new automatic progression rate system</span></div>
<div id="LC210" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-c"><span class="pl-c">#</span> Uses &quot;!= 2&quot; check to detect any save without the version 2 &quot;seal&quot;</span></div>
<div id="LC211" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">if</span> save_system_version <span class="pl-k">!=</span> <span class="pl-c1">2</span>:</div>
<div id="LC212" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">scene</span> black <span class="pl-k">with</span> dissolve</div>
<div id="LC213" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC214" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        centered <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{b}</span>Character Progression System Updated<span class="pl-c1">{/b}</span><span class="pl-cce">\n\n</span>We&#39;ve implemented an automatic character progression rate system<span class="pl-cce">\n</span>to make stat changes more consistent and balanced.<span class="pl-cce">\n\n</span><span class="pl-c1">{color=#ffcc00}</span>Your save will be automatically migrated.<span class="pl-c1">{/color}</span><span class="pl-cce">\n\n</span>Note: Due to technical limitations, the migration may not be 100%% perfect.<span class="pl-cce">\n</span>For the best experience, we recommend starting a new playthrough.<span class="pl-cce">\n\n</span>Press any key to continue...<span class="pl-pds">&quot;</span></span></div>
<div id="LC215" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC216" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">$</span> renpy.pause(<span class="pl-smi">hard</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</div>
<div id="LC217" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC218" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-c"><span class="pl-c">#</span> Perform the migration</span></div>
<div id="LC219" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">$</span> rm.migrate_to_ratio_system()</div>
<div id="LC220" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">$</span> save_system_version <span class="pl-k">=</span> <span class="pl-c1">2</span>  <span class="pl-c"><span class="pl-c">#</span> Apply version 2 &quot;seal&quot;</span></div>
<div id="LC221" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC222" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        centered <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{b}</span>Migration Complete<span class="pl-c1">{/b}</span><span class="pl-cce">\n\n</span>Your character stats have been adjusted to the new system.<span class="pl-cce">\n</span>Future stat changes will use automatic progression rates.<span class="pl-cce">\n\n</span>Press any key to continue...<span class="pl-pds">&quot;</span></span></div>
<div id="LC223" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC224" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">        <span class="pl-k">$</span> renpy.pause(<span class="pl-smi">hard</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</div>
<div id="LC225" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC226" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">    <span class="pl-k">return</span></div></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div><button hidden="" data-testid="hotkey-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></section></div></div></div> <!-- --> <!-- --> </div></div></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-62in7e-0 vdPNv"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>
</turbo-frame>



  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo" >
  <h2 class='sr-only'>Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</a>
      <span>
        &copy; 2025 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2" >
  <cookie-consent-link>
    <button
      type="button"
      class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent"
      data-action="click:cookie-consent-link#showConsentManagement"
      data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}"
    >
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link>
    <button
      type="button"
      class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left"
      data-action="click:cookie-consent-link#showConsentManagement"
      data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}"
    >
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999"
      data-locale="en"
      data-initial-cookie-consent-allowed=""
      data-cookie-consent-required="false"
    ></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>
<template id="snippet-clipboard-copy-button-unpositioned">
  <div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>


    <style>
      .user-mention[href$="/yukihina"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/yukihina"]:before,
      .user-mention[href$="/yukihina"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true" ></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  </body>
</html>

