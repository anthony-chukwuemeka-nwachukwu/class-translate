from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
@app.route('/about/')
def about():
	return render_template('about.html')
@app.route('/collections')
@app.route('/collections/')
def collections():
	return render_template('collections.html')
@app.route('/contact')
@app.route('/contact/')
def contact():
	return render_template('contact.html')
@app.route('/help')
@app.route('/help/')
def help():
	return render_template('help.html')
@app.route('/institutions')
@app.route('/institutions/')
def institutions():
	return render_template('institutions.html')
@app.route('/lists')
@app.route('/lists/')
def lists():
	return render_template('lists.html')
@app.route('/login')
@app.route('/login/')
def login():
	return render_template('login.html')
@app.route('/most-popular-courses')
@app.route('/most-popular-courses/')
def most_popular_courses():
	return render_template('most-popular-courses.html')
@app.route('/new-online-courses')
@app.route('/new-online-courses/')
def new_online_courses():
	return render_template('new-online-courses.html')
@app.route('/providers')
@app.route('/providers/')
def providers():
	return render_template('providers.html')
@app.route('/rankings')
@app.route('/rankings/')
def rankings():
	return render_template('rankings.html')
@app.route('/report')
@app.route('/report/')
def report():
	return render_template('report.html')
@app.route('/signup')
@app.route('/signup/')
def signup():
	return render_template('signup.html')
@app.route('/signupsignup_source=slidein%20desktop')
@app.route('/signupsignup_source=slidein%20desktop/')
def signupsignup_source_slidein_desktop():
	return render_template('signupsignup_source=slidein%20desktop.html')
@app.route('/starting-this-month')
@app.route('/starting-this-month/')
def starting_this_month():
	return render_template('starting-this-month.html')
@app.route('/subjects')
@app.route('/subjects/')
def subjects():
	return render_template('subjects.html')
@app.route('/universities')
@app.route('/universities/')
def universities():
	return render_template('universities.html')
@app.route('/about/careers')
@app.route('/about/careers/')
def about_careers():
	return render_template('about/careers.html')
@app.route('/about/privacy-policy')
@app.route('/about/privacy-policy/')
def about_privacy_policy():
	return render_template('about/privacy-policy.html')
@app.route('/collection/ivy-league-moocs')
@app.route('/collection/ivy-league-moocs/')
def collection_ivy_league_moocs():
	return render_template('collection/ivy-league-moocs.html')
@app.route('/collection/top-free-online-courses')
@app.route('/collection/top-free-online-courses/')
def collection_top_free_online_courses():
	return render_template('collection/top-free-online-courses.html')
@app.route('/course/build-a-computer-3234')
@app.route('/course/build-a-computer-3234/')
def course_build_a_computer_3234():
	return render_template('course/build-a-computer-3234.html')
@app.route('/course/digital-marketing-revolution-54370')
@app.route('/course/digital-marketing-revolution-54370/')
def course_digital_marketing_revolution_54370():
	return render_template('course/digital-marketing-revolution-54370.html')
@app.route('/course/dmdigitalworld-2750')
@app.route('/course/dmdigitalworld-2750/')
def course_dmdigitalworld_2750():
	return render_template('course/dmdigitalworld-2750.html')
@app.route('/course/edx-agile-innovation-and-problem-solving-skills-11919')
@app.route('/course/edx-agile-innovation-and-problem-solving-skills-11919/')
def course_edx_agile_innovation_and_problem_solving_skills_11919():
	return render_template('course/edx-agile-innovation-and-problem-solving-skills-11919.html')
@app.route('/course/edx-agile-leadership-principles-and-practices-11920')
@app.route('/course/edx-agile-leadership-principles-and-practices-11920/')
def course_edx_agile_leadership_principles_and_practices_11920():
	return render_template('course/edx-agile-leadership-principles-and-practices-11920.html')
@app.route('/course/edx-agile-process-project-and-program-controls-11921')
@app.route('/course/edx-agile-process-project-and-program-controls-11921/')
def course_edx_agile_process_project_and_program_controls_11921():
	return render_template('course/edx-agile-process-project-and-program-controls-11921.html')
@app.route('/course/edx-applied-scrum-for-agile-project-management-11917')
@app.route('/course/edx-applied-scrum-for-agile-project-management-11917/')
def course_edx_applied_scrum_for_agile_project_management_11917():
	return render_template('course/edx-applied-scrum-for-agile-project-management-11917.html')
@app.route('/course/edx-managing-conflicts-on-projects-with-cultural-and-emotional-intelligence-19747')
@app.route('/course/edx-managing-conflicts-on-projects-with-cultural-and-emotional-intelligence-19747/')
def course_edx_managing_conflicts_on_projects_with_cultural_and_emotional_intelligence_19747():
	return render_template('course/edx-managing-conflicts-on-projects-with-cultural-and-emotional-intelligence-19747.html')
@app.route('/course/edx-marketing-digital-content-community-manager-10386')
@app.route('/course/edx-marketing-digital-content-community-manager-10386/')
def course_edx_marketing_digital_content_community_manager_10386():
	return render_template('course/edx-marketing-digital-content-community-manager-10386.html')
@app.route('/course/edx-monitoring-volcanoes-and-magma-movements-13227')
@app.route('/course/edx-monitoring-volcanoes-and-magma-movements-13227/')
def course_edx_monitoring_volcanoes_and_magma_movements_13227():
	return render_template('course/edx-monitoring-volcanoes-and-magma-movements-13227.html')
@app.route('/course/edx-product-management-fundamentals-19098')
@app.route('/course/edx-product-management-fundamentals-19098/')
def course_edx_product_management_fundamentals_19098():
	return render_template('course/edx-product-management-fundamentals-19098.html')
@app.route('/course/edx-six-sigma-define-and-measure-8450')
@app.route('/course/edx-six-sigma-define-and-measure-8450/')
def course_edx_six_sigma_define_and_measure_8450():
	return render_template('course/edx-six-sigma-define-and-measure-8450.html')
@app.route('/course/edx-sprint-planning-for-faster-agile-team-delivery-11918')
@app.route('/course/edx-sprint-planning-for-faster-agile-team-delivery-11918/')
def course_edx_sprint_planning_for_faster_agile_team_delivery_11918():
	return render_template('course/edx-sprint-planning-for-faster-agile-team-delivery-11918.html')
@app.route('/course/edx-sustainable-tourism-society-environmental-aspects-10356')
@app.route('/course/edx-sustainable-tourism-society-environmental-aspects-10356/')
def course_edx_sustainable_tourism_society_environmental_aspects_10356():
	return render_template('course/edx-sustainable-tourism-society-environmental-aspects-10356.html')
@app.route('/course/fintech-11193')
@app.route('/course/fintech-11193/')
def course_fintech_11193():
	return render_template('course/fintech-11193.html')
@app.route('/course/managing-human-resources-5462')
@app.route('/course/managing-human-resources-5462/')
def course_managing_human_resources_5462():
	return render_template('course/managing-human-resources-5462.html')
@app.route('/course/protect-business-innovations-patent-10382')
@app.route('/course/protect-business-innovations-patent-10382/')
def course_protect_business_innovations_patent_10382():
	return render_template('course/protect-business-innovations-patent-10382.html')
@app.route('/course/success-8087')
@app.route('/course/success-8087/')
def course_success_8087():
	return render_template('course/success-8087.html')
@app.route('/institution/amazon')
@app.route('/institution/amazon/')
def institution_amazon():
	return render_template('institution/amazon.html')
@app.route('/institution/british-council')
@app.route('/institution/british-council/')
def institution_british_council():
	return render_template('institution/british-council.html')
@app.route('/institution/google')
@app.route('/institution/google/')
def institution_google():
	return render_template('institution/google.html')
@app.route('/institution/ibm')
@app.route('/institution/ibm/')
def institution_ibm():
	return render_template('institution/ibm.html')
@app.route('/institution/linuxfoundation')
@app.route('/institution/linuxfoundation/')
def institution_linuxfoundation():
	return render_template('institution/linuxfoundation.html')
@app.route('/institution/microsoft')
@app.route('/institution/microsoft/')
def institution_microsoft():
	return render_template('institution/microsoft.html')
@app.route('/institution/salesforce')
@app.route('/institution/salesforce/')
def institution_salesforce():
	return render_template('institution/salesforce.html')
@app.route('/provider/coursera')
@app.route('/provider/coursera/')
def provider_coursera():
	return render_template('provider/coursera.html')
@app.route('/provider/edx')
@app.route('/provider/edx/')
def provider_edx():
	return render_template('provider/edx.html')
@app.route('/provider/futurelearn')
@app.route('/provider/futurelearn/')
def provider_futurelearn():
	return render_template('provider/futurelearn.html')
@app.route('/provider/linkedin-learning')
@app.route('/provider/linkedin-learning/')
def provider_linkedin_learning():
	return render_template('provider/linkedin-learning.html')
@app.route('/provider/swayam')
@app.route('/provider/swayam/')
def provider_swayam():
	return render_template('provider/swayam.html')
@app.route('/provider/udacity')
@app.route('/provider/udacity/')
def provider_udacity():
	return render_template('provider/udacity.html')
@app.route('/provider/udemy')
@app.route('/provider/udemy/')
def provider_udemy():
	return render_template('provider/udemy.html')
@app.route('/report/100-most-popular-online-courses-2021')
@app.route('/report/100-most-popular-online-courses-2021/')
def report_100_most_popular_online_courses_2021():
	return render_template('report/100-most-popular-online-courses-2021.html')
@app.route('/report/2022-year-in-review')
@app.route('/report/2022-year-in-review/')
def report_2022_year_in_review():
	return render_template('report/2022-year-in-review.html')
@app.route('/report/best-digital-art-courses')
@app.route('/report/best-digital-art-courses/')
def report_best_digital_art_courses():
	return render_template('report/best-digital-art-courses.html')
@app.route('/report/best-elm-courses')
@app.route('/report/best-elm-courses/')
def report_best_elm_courses():
	return render_template('report/best-elm-courses.html')
@app.route('/report/best-free-online-courses-2021')
@app.route('/report/best-free-online-courses-2021/')
def report_best_free_online_courses_2021():
	return render_template('report/best-free-online-courses-2021.html')
@app.route('/report/best-free-online-courses-2022')
@app.route('/report/best-free-online-courses-2022/')
def report_best_free_online_courses_2022():
	return render_template('report/best-free-online-courses-2022.html')
@app.route('/report/class-central-ddos-attack')
@app.route('/report/class-central-ddos-attack/')
def report_class_central_ddos_attack():
	return render_template('report/class-central-ddos-attack.html')
@app.route('/report/coursera-free-online-courses')
@app.route('/report/coursera-free-online-courses/')
def report_coursera_free_online_courses():
	return render_template('report/coursera-free-online-courses.html')
@app.route('/report/coursera-top-courses')
@app.route('/report/coursera-top-courses/')
def report_coursera_top_courses():
	return render_template('report/coursera-top-courses.html')
@app.route('/report/cs50-free-certificate')
@app.route('/report/cs50-free-certificate/')
def report_cs50_free_certificate():
	return render_template('report/cs50-free-certificate.html')
@app.route('/report/edx-top-courses')
@app.route('/report/edx-top-courses/')
def report_edx_top_courses():
	return render_template('report/edx-top-courses.html')
@app.route('/report/emoocs-2023-cfp')
@app.route('/report/emoocs-2023-cfp/')
def report_emoocs_2023_cfp():
	return render_template('report/emoocs-2023-cfp.html')
@app.route('/report/free-certificates')
@app.route('/report/free-certificates/')
def report_free_certificates():
	return render_template('report/free-certificates.html')
@app.route('/report/free-google-certifications')
@app.route('/report/free-google-certifications/')
def report_free_google_certifications():
	return render_template('report/free-google-certifications.html')
@app.route('/report/google-free-certificates')
@app.route('/report/google-free-certificates/')
def report_google_free_certificates():
	return render_template('report/google-free-certificates.html')
@app.route('/report/india-online-degrees')
@app.route('/report/india-online-degrees/')
def report_india_online_degrees():
	return render_template('report/india-online-degrees.html')
@app.route('/report/linkedin-learning-free-learning-paths')
@app.route('/report/linkedin-learning-free-learning-paths/')
def report_linkedin_learning_free_learning_paths():
	return render_template('report/linkedin-learning-free-learning-paths.html')
@app.route('/report/most-cited-mooc-research')
@app.route('/report/most-cited-mooc-research/')
def report_most_cited_mooc_research():
	return render_template('report/most-cited-mooc-research.html')
@app.route('/report/most-popular-courses-2022')
@app.route('/report/most-popular-courses-2022/')
def report_most_popular_courses_2022():
	return render_template('report/most-popular-courses-2022.html')
@app.route('/report/most-popular-courses-2023')
@app.route('/report/most-popular-courses-2023/')
def report_most_popular_courses_2023():
	return render_template('report/most-popular-courses-2023.html')
@app.route('/report/most-popular-online-courses')
@app.route('/report/most-popular-online-courses/')
def report_most_popular_online_courses():
	return render_template('report/most-popular-online-courses.html')
@app.route('/report/open-university-insiders-perspective')
@app.route('/report/open-university-insiders-perspective/')
def report_open_university_insiders_perspective():
	return render_template('report/open-university-insiders-perspective.html')
@app.route('/report/review-china-economic-transformation')
@app.route('/report/review-china-economic-transformation/')
def report_review_china_economic_transformation():
	return render_template('report/review-china-economic-transformation.html')
@app.route('/report/udemy-top-courses')
@app.route('/report/udemy-top-courses/')
def report_udemy_top_courses():
	return render_template('report/udemy-top-courses.html')
@app.route('/report/writing-free-online-courses')
@app.route('/report/writing-free-online-courses/')
def report_writing_free_online_courses():
	return render_template('report/writing-free-online-courses.html')
@app.route('/report/author/dhawal')
@app.route('/report/author/dhawal/')
def report_author_dhawal():
	return render_template('report/author/dhawal.html')
@app.route('/subject/accounting')
@app.route('/subject/accounting/')
def subject_accounting():
	return render_template('subject/accounting.html')
@app.route('/subject/aerospace-engineering')
@app.route('/subject/aerospace-engineering/')
def subject_aerospace_engineering():
	return render_template('subject/aerospace-engineering.html')
@app.route('/subject/agriculture')
@app.route('/subject/agriculture/')
def subject_agriculture():
	return render_template('subject/agriculture.html')
@app.route('/subject/ai')
@app.route('/subject/ai/')
def subject_ai():
	return render_template('subject/ai.html')
@app.route('/subject/algebra')
@app.route('/subject/algebra/')
def subject_algebra():
	return render_template('subject/algebra.html')
@app.route('/subject/algorithms-and-data-structures')
@app.route('/subject/algorithms-and-data-structures/')
def subject_algorithms_and_data_structures():
	return render_template('subject/algorithms-and-data-structures.html')
@app.route('/subject/anatomy')
@app.route('/subject/anatomy/')
def subject_anatomy():
	return render_template('subject/anatomy.html')
@app.route('/subject/anthropology')
@app.route('/subject/anthropology/')
def subject_anthropology():
	return render_template('subject/anthropology.html')
@app.route('/subject/applied-science')
@app.route('/subject/applied-science/')
def subject_applied_science():
	return render_template('subject/applied-science.html')
@app.route('/subject/archaeology')
@app.route('/subject/archaeology/')
def subject_archaeology():
	return render_template('subject/archaeology.html')
@app.route('/subject/art-and-design')
@app.route('/subject/art-and-design/')
def subject_art_and_design():
	return render_template('subject/art-and-design.html')
@app.route('/subject/astronomy')
@app.route('/subject/astronomy/')
def subject_astronomy():
	return render_template('subject/astronomy.html')
@app.route('/subject/big-data')
@app.route('/subject/big-data/')
def subject_big_data():
	return render_template('subject/big-data.html')
@app.route('/subject/bim')
@app.route('/subject/bim/')
def subject_bim():
	return render_template('subject/bim.html')
@app.route('/subject/bioinformatics')
@app.route('/subject/bioinformatics/')
def subject_bioinformatics():
	return render_template('subject/bioinformatics.html')
@app.route('/subject/biology')
@app.route('/subject/biology/')
def subject_biology():
	return render_template('subject/biology.html')
@app.route('/subject/blockchain')
@app.route('/subject/blockchain/')
def subject_blockchain():
	return render_template('subject/blockchain.html')
@app.route('/subject/blue-team')
@app.route('/subject/blue-team/')
def subject_blue_team():
	return render_template('subject/blue-team.html')
@app.route('/subject/business-analysis')
@app.route('/subject/business-analysis/')
def subject_business_analysis():
	return render_template('subject/business-analysis.html')
@app.route('/subject/business-intelligence')
@app.route('/subject/business-intelligence/')
def subject_business_intelligence():
	return render_template('subject/business-intelligence.html')
@app.route('/subject/business-software')
@app.route('/subject/business-software/')
def subject_business_software():
	return render_template('subject/business-software.html')
@app.route('/subject/business')
@app.route('/subject/business/')
def subject_business():
	return render_template('subject/business.html')
@app.route('/subject/cad')
@app.route('/subject/cad/')
def subject_cad():
	return render_template('subject/cad.html')
@app.route('/subject/calculus')
@app.route('/subject/calculus/')
def subject_calculus():
	return render_template('subject/calculus.html')
@app.route('/subject/career-development')
@app.route('/subject/career-development/')
def subject_career_development():
	return render_template('subject/career-development.html')
@app.route('/subject/chemical-engineering')
@app.route('/subject/chemical-engineering/')
def subject_chemical_engineering():
	return render_template('subject/chemical-engineering.html')
@app.route('/subject/chemistry')
@app.route('/subject/chemistry/')
def subject_chemistry():
	return render_template('subject/chemistry.html')
@app.route('/subject/childhood-development')
@app.route('/subject/childhood-development/')
def subject_childhood_development():
	return render_template('subject/childhood-development.html')
@app.route('/subject/civil-engineering')
@app.route('/subject/civil-engineering/')
def subject_civil_engineering():
	return render_template('subject/civil-engineering.html')
@app.route('/subject/cloud-computing')
@app.route('/subject/cloud-computing/')
def subject_cloud_computing():
	return render_template('subject/cloud-computing.html')
@app.route('/subject/cme')
@app.route('/subject/cme/')
def subject_cme():
	return render_template('subject/cme.html')
@app.route('/subject/combinatorics')
@app.route('/subject/combinatorics/')
def subject_combinatorics():
	return render_template('subject/combinatorics.html')
@app.route('/subject/communication-skills')
@app.route('/subject/communication-skills/')
def subject_communication_skills():
	return render_template('subject/communication-skills.html')
@app.route('/subject/computer-graphics')
@app.route('/subject/computer-graphics/')
def subject_computer_graphics():
	return render_template('subject/computer-graphics.html')
@app.route('/subject/computer-networking')
@app.route('/subject/computer-networking/')
def subject_computer_networking():
	return render_template('subject/computer-networking.html')
@app.route('/subject/course-development')
@app.route('/subject/course-development/')
def subject_course_development():
	return render_template('subject/course-development.html')
@app.route('/subject/crisis-management')
@app.route('/subject/crisis-management/')
def subject_crisis_management():
	return render_template('subject/crisis-management.html')
@app.route('/subject/cryptography')
@app.route('/subject/cryptography/')
def subject_cryptography():
	return render_template('subject/cryptography.html')
@app.route('/subject/cs')
@app.route('/subject/cs/')
def subject_cs():
	return render_template('subject/cs.html')
@app.route('/subject/csr')
@app.route('/subject/csr/')
def subject_csr():
	return render_template('subject/csr.html')
@app.route('/subject/culture')
@app.route('/subject/culture/')
def subject_culture():
	return render_template('subject/culture.html')
@app.route('/subject/customer-service')
@app.route('/subject/customer-service/')
def subject_customer_service():
	return render_template('subject/customer-service.html')
@app.route('/subject/cybersecurity')
@app.route('/subject/cybersecurity/')
def subject_cybersecurity():
	return render_template('subject/cybersecurity.html')
@app.route('/subject/data-analysis')
@app.route('/subject/data-analysis/')
def subject_data_analysis():
	return render_template('subject/data-analysis.html')
@app.route('/subject/data-mining')
@app.route('/subject/data-mining/')
def subject_data_mining():
	return render_template('subject/data-mining.html')
@app.route('/subject/data-science')
@app.route('/subject/data-science/')
def subject_data_science():
	return render_template('subject/data-science.html')
@app.route('/subject/data-visualization')
@app.route('/subject/data-visualization/')
def subject_data_visualization():
	return render_template('subject/data-visualization.html')
@app.route('/subject/databases')
@app.route('/subject/databases/')
def subject_databases():
	return render_template('subject/databases.html')
@app.route('/subject/deep-learning')
@app.route('/subject/deep-learning/')
def subject_deep_learning():
	return render_template('subject/deep-learning.html')
@app.route('/subject/design-and-creativity')
@app.route('/subject/design-and-creativity/')
def subject_design_and_creativity():
	return render_template('subject/design-and-creativity.html')
@app.route('/subject/design-thinking')
@app.route('/subject/design-thinking/')
def subject_design_thinking():
	return render_template('subject/design-thinking.html')
@app.route('/subject/devops')
@app.route('/subject/devops/')
def subject_devops():
	return render_template('subject/devops.html')
@app.route('/subject/devsecops')
@app.route('/subject/devsecops/')
def subject_devsecops():
	return render_template('subject/devsecops.html')
@app.route('/subject/digital-forensics')
@app.route('/subject/digital-forensics/')
def subject_digital_forensics():
	return render_template('subject/digital-forensics.html')
@app.route('/subject/digital-media')
@app.route('/subject/digital-media/')
def subject_digital_media():
	return render_template('subject/digital-media.html')
@app.route('/subject/digital-skills')
@app.route('/subject/digital-skills/')
def subject_digital_skills():
	return render_template('subject/digital-skills.html')
@app.route('/subject/discrete-mathematics')
@app.route('/subject/discrete-mathematics/')
def subject_discrete_mathematics():
	return render_template('subject/discrete-mathematics.html')
@app.route('/subject/disease-and-disorders')
@app.route('/subject/disease-and-disorders/')
def subject_disease_and_disorders():
	return render_template('subject/disease-and-disorders.html')
@app.route('/subject/distributed-systems')
@app.route('/subject/distributed-systems/')
def subject_distributed_systems():
	return render_template('subject/distributed-systems.html')
@app.route('/subject/earth-science')
@app.route('/subject/earth-science/')
def subject_earth_science():
	return render_template('subject/earth-science.html')
@app.route('/subject/economics')
@app.route('/subject/economics/')
def subject_economics():
	return render_template('subject/economics.html')
@app.route('/subject/education')
@app.route('/subject/education/')
def subject_education():
	return render_template('subject/education.html')
@app.route('/subject/electrical-engineering')
@app.route('/subject/electrical-engineering/')
def subject_electrical_engineering():
	return render_template('subject/electrical-engineering.html')
@app.route('/subject/energy-systems')
@app.route('/subject/energy-systems/')
def subject_energy_systems():
	return render_template('subject/energy-systems.html')
@app.route('/subject/engineering')
@app.route('/subject/engineering/')
def subject_engineering():
	return render_template('subject/engineering.html')
@app.route('/subject/entrepreneurship')
@app.route('/subject/entrepreneurship/')
def subject_entrepreneurship():
	return render_template('subject/entrepreneurship.html')
@app.route('/subject/environmental-science')
@app.route('/subject/environmental-science/')
def subject_environmental_science():
	return render_template('subject/environmental-science.html')
@app.route('/subject/esl')
@app.route('/subject/esl/')
def subject_esl():
	return render_template('subject/esl.html')
@app.route('/subject/ethical-hacking')
@app.route('/subject/ethical-hacking/')
def subject_ethical_hacking():
	return render_template('subject/ethical-hacking.html')
@app.route('/subject/ethics')
@app.route('/subject/ethics/')
def subject_ethics():
	return render_template('subject/ethics.html')
@app.route('/subject/finance')
@app.route('/subject/finance/')
def subject_finance():
	return render_template('subject/finance.html')
@app.route('/subject/food')
@app.route('/subject/food/')
def subject_food():
	return render_template('subject/food.html')
@app.route('/subject/forensic-science')
@app.route('/subject/forensic-science/')
def subject_forensic_science():
	return render_template('subject/forensic-science.html')
@app.route('/subject/foundations-of-mathematics')
@app.route('/subject/foundations-of-mathematics/')
def subject_foundations_of_mathematics():
	return render_template('subject/foundations-of-mathematics.html')
@app.route('/subject/game-development')
@app.route('/subject/game-development/')
def subject_game_development():
	return render_template('subject/game-development.html')
@app.route('/subject/geometry')
@app.route('/subject/geometry/')
def subject_geometry():
	return render_template('subject/geometry.html')
@app.route('/subject/gis')
@app.route('/subject/gis/')
def subject_gis():
	return render_template('subject/gis.html')
@app.route('/subject/governance')
@app.route('/subject/governance/')
def subject_governance():
	return render_template('subject/governance.html')
@app.route('/subject/grammar-writing')
@app.route('/subject/grammar-writing/')
def subject_grammar_writing():
	return render_template('subject/grammar-writing.html')
@app.route('/subject/hci')
@app.route('/subject/hci/')
def subject_hci():
	return render_template('subject/hci.html')
@app.route('/subject/health-care')
@app.route('/subject/health-care/')
def subject_health_care():
	return render_template('subject/health-care.html')
@app.route('/subject/health')
@app.route('/subject/health/')
def subject_health():
	return render_template('subject/health.html')
@app.route('/subject/higher-education')
@app.route('/subject/higher-education/')
def subject_higher_education():
	return render_template('subject/higher-education.html')
@app.route('/subject/history')
@app.route('/subject/history/')
def subject_history():
	return render_template('subject/history.html')
@app.route('/subject/human-resources')
@app.route('/subject/human-resources/')
def subject_human_resources():
	return render_template('subject/human-resources.html')
@app.route('/subject/human-rights')
@app.route('/subject/human-rights/')
def subject_human_rights():
	return render_template('subject/human-rights.html')
@app.route('/subject/humanities')
@app.route('/subject/humanities/')
def subject_humanities():
	return render_template('subject/humanities.html')
@app.route('/subject/industry-specific')
@app.route('/subject/industry-specific/')
def subject_industry_specific():
	return render_template('subject/industry-specific.html')
@app.route('/subject/information-technology')
@app.route('/subject/information-technology/')
def subject_information_technology():
	return render_template('subject/information-technology.html')
@app.route('/subject/infosec-certifications')
@app.route('/subject/infosec-certifications/')
def subject_infosec_certifications():
	return render_template('subject/infosec-certifications.html')
@app.route('/subject/infosec')
@app.route('/subject/infosec/')
def subject_infosec():
	return render_template('subject/infosec.html')
@app.route('/subject/innovation')
@app.route('/subject/innovation/')
def subject_innovation():
	return render_template('subject/innovation.html')
@app.route('/subject/internet-of-things')
@app.route('/subject/internet-of-things/')
def subject_internet_of_things():
	return render_template('subject/internet-of-things.html')
@app.route('/subject/journalism')
@app.route('/subject/journalism/')
def subject_journalism():
	return render_template('subject/journalism.html')
@app.route('/subject/jupyter')
@app.route('/subject/jupyter/')
def subject_jupyter():
	return render_template('subject/jupyter.html')
@app.route('/subject/k12')
@app.route('/subject/k12/')
def subject_k12():
	return render_template('subject/k12.html')
@app.route('/subject/language-learning')
@app.route('/subject/language-learning/')
def subject_language_learning():
	return render_template('subject/language-learning.html')
@app.route('/subject/law')
@app.route('/subject/law/')
def subject_law():
	return render_template('subject/law.html')
@app.route('/subject/leadership')
@app.route('/subject/leadership/')
def subject_leadership():
	return render_template('subject/leadership.html')
@app.route('/subject/library-science')
@app.route('/subject/library-science/')
def subject_library_science():
	return render_template('subject/library-science.html')
@app.route('/subject/linear-programming')
@app.route('/subject/linear-programming/')
def subject_linear_programming():
	return render_template('subject/linear-programming.html')
@app.route('/subject/linguistics')
@app.route('/subject/linguistics/')
def subject_linguistics():
	return render_template('subject/linguistics.html')
@app.route('/subject/literature')
@app.route('/subject/literature/')
def subject_literature():
	return render_template('subject/literature.html')
@app.route('/subject/machine-learning')
@app.route('/subject/machine-learning/')
def subject_machine_learning():
	return render_template('subject/machine-learning.html')
@app.route('/subject/malware-analysis')
@app.route('/subject/malware-analysis/')
def subject_malware_analysis():
	return render_template('subject/malware-analysis.html')
@app.route('/subject/management-and-leadership')
@app.route('/subject/management-and-leadership/')
def subject_management_and_leadership():
	return render_template('subject/management-and-leadership.html')
@app.route('/subject/manufacturing')
@app.route('/subject/manufacturing/')
def subject_manufacturing():
	return render_template('subject/manufacturing.html')
@app.route('/subject/marketing')
@app.route('/subject/marketing/')
def subject_marketing():
	return render_template('subject/marketing.html')
@app.route('/subject/materials-science')
@app.route('/subject/materials-science/')
def subject_materials_science():
	return render_template('subject/materials-science.html')
@app.route('/subject/mathematical-logic')
@app.route('/subject/mathematical-logic/')
def subject_mathematical_logic():
	return render_template('subject/mathematical-logic.html')
@app.route('/subject/maths')
@app.route('/subject/maths/')
def subject_maths():
	return render_template('subject/maths.html')
@app.route('/subject/mechanical-engineering')
@app.route('/subject/mechanical-engineering/')
def subject_mechanical_engineering():
	return render_template('subject/mechanical-engineering.html')
@app.route('/subject/mobile-development')
@app.route('/subject/mobile-development/')
def subject_mobile_development():
	return render_template('subject/mobile-development.html')
@app.route('/subject/music')
@app.route('/subject/music/')
def subject_music():
	return render_template('subject/music.html')
@app.route('/subject/nanotechnology')
@app.route('/subject/nanotechnology/')
def subject_nanotechnology():
	return render_template('subject/nanotechnology.html')
@app.route('/subject/network-security')
@app.route('/subject/network-security/')
def subject_network_security():
	return render_template('subject/network-security.html')
@app.route('/subject/nonprofit')
@app.route('/subject/nonprofit/')
def subject_nonprofit():
	return render_template('subject/nonprofit.html')
@app.route('/subject/number-theory')
@app.route('/subject/number-theory/')
def subject_number_theory():
	return render_template('subject/number-theory.html')
@app.route('/subject/nursing')
@app.route('/subject/nursing/')
def subject_nursing():
	return render_template('subject/nursing.html')
@app.route('/subject/nutrition-and-wellness')
@app.route('/subject/nutrition-and-wellness/')
def subject_nutrition_and_wellness():
	return render_template('subject/nutrition-and-wellness.html')
@app.route('/subject/online-education')
@app.route('/subject/online-education/')
def subject_online_education():
	return render_template('subject/online-education.html')
@app.route('/subject/operating-systems')
@app.route('/subject/operating-systems/')
def subject_operating_systems():
	return render_template('subject/operating-systems.html')
@app.route('/subject/operations-management')
@app.route('/subject/operations-management/')
def subject_operations_management():
	return render_template('subject/operations-management.html')
@app.route('/subject/osint')
@app.route('/subject/osint/')
def subject_osint():
	return render_template('subject/osint.html')
@app.route('/subject/pedagogy')
@app.route('/subject/pedagogy/')
def subject_pedagogy():
	return render_template('subject/pedagogy.html')
@app.route('/subject/pentesting')
@app.route('/subject/pentesting/')
def subject_pentesting():
	return render_template('subject/pentesting.html')
@app.route('/subject/personal-development')
@app.route('/subject/personal-development/')
def subject_personal_development():
	return render_template('subject/personal-development.html')
@app.route('/subject/philosophy')
@app.route('/subject/philosophy/')
def subject_philosophy():
	return render_template('subject/philosophy.html')
@app.route('/subject/physics')
@app.route('/subject/physics/')
def subject_physics():
	return render_template('subject/physics.html')
@app.route('/subject/political-science')
@app.route('/subject/political-science/')
def subject_political_science():
	return render_template('subject/political-science.html')
@app.route('/subject/precalculus')
@app.route('/subject/precalculus/')
def subject_precalculus():
	return render_template('subject/precalculus.html')
@app.route('/subject/presentation-skills')
@app.route('/subject/presentation-skills/')
def subject_presentation_skills():
	return render_template('subject/presentation-skills.html')
@app.route('/subject/product-management')
@app.route('/subject/product-management/')
def subject_product_management():
	return render_template('subject/product-management.html')
@app.route('/subject/programming-and-software-development')
@app.route('/subject/programming-and-software-development/')
def subject_programming_and_software_development():
	return render_template('subject/programming-and-software-development.html')
@app.route('/subject/programming-languages')
@app.route('/subject/programming-languages/')
def subject_programming_languages():
	return render_template('subject/programming-languages.html')
@app.route('/subject/project-management')
@app.route('/subject/project-management/')
def subject_project_management():
	return render_template('subject/project-management.html')
@app.route('/subject/psychology')
@app.route('/subject/psychology/')
def subject_psychology():
	return render_template('subject/psychology.html')
@app.route('/subject/public-health')
@app.route('/subject/public-health/')
def subject_public_health():
	return render_template('subject/public-health.html')
@app.route('/subject/quantum-computing')
@app.route('/subject/quantum-computing/')
def subject_quantum_computing():
	return render_template('subject/quantum-computing.html')
@app.route('/subject/reading')
@app.route('/subject/reading/')
def subject_reading():
	return render_template('subject/reading.html')
@app.route('/subject/red-team')
@app.route('/subject/red-team/')
def subject_red_team():
	return render_template('subject/red-team.html')
@app.route('/subject/religion')
@app.route('/subject/religion/')
def subject_religion():
	return render_template('subject/religion.html')
@app.route('/subject/resilience')
@app.route('/subject/resilience/')
def subject_resilience():
	return render_template('subject/resilience.html')
@app.route('/subject/reverse-engineering')
@app.route('/subject/reverse-engineering/')
def subject_reverse_engineering():
	return render_template('subject/reverse-engineering.html')
@app.route('/subject/risk-management')
@app.route('/subject/risk-management/')
def subject_risk_management():
	return render_template('subject/risk-management.html')
@app.route('/subject/robotics')
@app.route('/subject/robotics/')
def subject_robotics():
	return render_template('subject/robotics.html')
@app.route('/subject/sales')
@app.route('/subject/sales/')
def subject_sales():
	return render_template('subject/sales.html')
@app.route('/subject/science')
@app.route('/subject/science/')
def subject_science():
	return render_template('subject/science.html')
@app.route('/subject/self-improvement')
@app.route('/subject/self-improvement/')
def subject_self_improvement():
	return render_template('subject/self-improvement.html')
@app.route('/subject/social-sciences')
@app.route('/subject/social-sciences/')
def subject_social_sciences():
	return render_template('subject/social-sciences.html')
@app.route('/subject/social-work')
@app.route('/subject/social-work/')
def subject_social_work():
	return render_template('subject/social-work.html')
@app.route('/subject/sociology')
@app.route('/subject/sociology/')
def subject_sociology():
	return render_template('subject/sociology.html')
@app.route('/subject/software-development')
@app.route('/subject/software-development/')
def subject_software_development():
	return render_template('subject/software-development.html')
@app.route('/subject/sports')
@app.route('/subject/sports/')
def subject_sports():
	return render_template('subject/sports.html')
@app.route('/subject/sql')
@app.route('/subject/sql/')
def subject_sql():
	return render_template('subject/sql.html')
@app.route('/subject/statistics')
@app.route('/subject/statistics/')
def subject_statistics():
	return render_template('subject/statistics.html')
@app.route('/subject/stem')
@app.route('/subject/stem/')
def subject_stem():
	return render_template('subject/stem.html')
@app.route('/subject/strategic-management')
@app.route('/subject/strategic-management/')
def subject_strategic_management():
	return render_template('subject/strategic-management.html')
@app.route('/subject/sustainability')
@app.route('/subject/sustainability/')
def subject_sustainability():
	return render_template('subject/sustainability.html')
@app.route('/subject/teacher-development')
@app.route('/subject/teacher-development/')
def subject_teacher_development():
	return render_template('subject/teacher-development.html')
@app.route('/subject/test-prep')
@app.route('/subject/test-prep/')
def subject_test_prep():
	return render_template('subject/test-prep.html')
@app.route('/subject/textiles')
@app.route('/subject/textiles/')
def subject_textiles():
	return render_template('subject/textiles.html')
@app.route('/subject/threat-intelligence')
@app.route('/subject/threat-intelligence/')
def subject_threat_intelligence():
	return render_template('subject/threat-intelligence.html')
@app.route('/subject/trigonometry')
@app.route('/subject/trigonometry/')
def subject_trigonometry():
	return render_template('subject/trigonometry.html')
@app.route('/subject/urban-planning')
@app.route('/subject/urban-planning/')
def subject_urban_planning():
	return render_template('subject/urban-planning.html')
@app.route('/subject/veterinary-science')
@app.route('/subject/veterinary-science/')
def subject_veterinary_science():
	return render_template('subject/veterinary-science.html')
@app.route('/subject/visual-arts')
@app.route('/subject/visual-arts/')
def subject_visual_arts():
	return render_template('subject/visual-arts.html')
@app.route('/subject/web-development')
@app.route('/subject/web-development/')
def subject_web_development():
	return render_template('subject/web-development.html')
@app.route('/university/duke')
@app.route('/university/duke/')
def university_duke():
	return render_template('university/duke.html')
@app.route('/university/galileo')
@app.route('/university/galileo/')
def university_galileo():
	return render_template('university/galileo.html')
@app.route('/university/gatech')
@app.route('/university/gatech/')
def university_gatech():
	return render_template('university/gatech.html')
@app.route('/university/harvard')
@app.route('/university/harvard/')
def university_harvard():
	return render_template('university/harvard.html')
@app.route('/university/hkust')
@app.route('/university/hkust/')
def university_hkust():
	return render_template('university/hkust.html')
@app.route('/university/iitm')
@app.route('/university/iitm/')
def university_iitm():
	return render_template('university/iitm.html')
@app.route('/university/illinois')
@app.route('/university/illinois/')
def university_illinois():
	return render_template('university/illinois.html')
@app.route('/university/minnesota')
@app.route('/university/minnesota/')
def university_minnesota():
	return render_template('university/minnesota.html')
@app.route('/university/purdue')
@app.route('/university/purdue/')
def university_purdue():
	return render_template('university/purdue.html')
@app.route('/university/stanford')
@app.route('/university/stanford/')
def university_stanford():
	return render_template('university/stanford.html')
@app.route('/university/tum')
@app.route('/university/tum/')
def university_tum():
	return render_template('university/tum.html')
@app.route('/university/umd')
@app.route('/university/umd/')
def university_umd():
	return render_template('university/umd.html')
@app.route('/university/umich')
@app.route('/university/umich/')
def university_umich():
	return render_template('university/umich.html')
@app.route('/university/usmd')
@app.route('/university/usmd/')
def university_usmd():
	return render_template('university/usmd.html')
@app.route('/university/wageningenur')
@app.route('/university/wageningenur/')
def university_wageningenur():
	return render_template('university/wageningenur.html')
