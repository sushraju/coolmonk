"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = '<p><li>Varied experience in scalable cloud infrastructure, distributed systems, product development, technology management and customer success across America, Europe and Asia. <li>Responsible for building stable and reliable data pipelines across the globe that led to increased customer adoption. <li>Executed customer success plans for large scale deployments that resulted in increased hardware revenue. <li>Mentored and led engineering teams that delivered projects for problems in performance, scale, reliability and data management.</p>'

education = [
        ['Masters in Computer Science & Applications', 'Bharathiyar University', '1996 - 1999'],
        ['BSc in Computer Science', 'Bharathiyar University', '1993 - 1996']
        ]

interests = ['jazz','travel','tech','wine','animals']

skills = [
        ['distributed systems', '80%'],
        ['python, perl & shell scripting', '85%'],
        ['linux, solaris', '85%'],
        ['aws, gcp, oci', '80%'],
        ['kafka, sqs, pub-sub', '75%'],
        ['redis, solr and elk', '70%'],
        ['chef, terraform', '75%'],
        ['kubernetes, docker', '70%'],
        ['git, mercurial', '80%']
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
        ['Site Reliability Engineering',
            'Jun 2020 – present',
            'Optimizely, San Francisco',
            '<p><li>performance, reliability, cdn, dns, data infrastructure and automation.</p>'
        ],
        ['Senior Manager, Platform & Infrastructure',
            'Jun 2019 – Feb 2020',
            'Reltio, Redwood Shores',
            '<p><li>Built and managed large scalable infrastructure for a cloud native MDM SaaS platform using a variety of services on AWS and GCP. <li>Responsible for automation, scale, performance and observability of the cloud infrastructure and software stack with cassandra and elasticsearch. <li>Led a distributed team of engineers working on different parts of the data infrastructure. Implemented standard SRE principles providing 24x7 support operations.</p>'
        ],
        ['Senior Manager, Oracle Management Cloud',
            'Dec 2015 - May 2019',
            'Oracle, Redwood Shores',
            '<p><li>Built a successful DevOps / SRE for a monitoring and analytics platform spread across the globe. Ownership of observability for cdn, eum, apm, logs, security and monitoring.<li>Built scaleable and performant infrastructure for accelerated promotion of services to production.<li>Complete ownership of deployment, process automation and observability of the full stack and hadoop / kafka clusters.</p>',
        ],
        ['Technology management, open source & other engagements',
            'Nov 2005 - Nov 2015',
            'Oracle / Sun, SF Bay area / Prague / Bangalore',
            '<p><li>Led and executed projects in data center management.<li>Defined and executed crisis management engagements at complex environments that resulted in millions of dollars in revenue.<li>Eclipse for Solaris x86 (official committer for Sun Microsystems).<li>Represented Sun in conferences and universities for datacenter management.<li:Implemented process and innovation initiatives for technology teams.</p>',
        ],
        ['Lead Systems Engineer',
            'Jun 1999 - Oct 2005',
            'Tata Infotech Ltd., Bangalore / Chicago',
            '<p><li>Defined, managed and executed on various SOWs (Statement of Work) for Ascom, QualComm and WorldBook. <li>Liaised with teams on-site and Tata Infotech’s offshore technology development team.</p>'
        ]
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
project_intro = '<p>You can list your side projects or open source libraries in this section. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula in nunc bibendum fringilla a eu lectus.</p>'
projects = []

"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
resume_data = {
    'site_title' : 'CoolMonk',
    'name' : 'Suresh Raju',
    'tagline' : 'Scaleable infrastructure & Site reliability',
    'website' : 'https://coolmonk.org',
    'linkedin' : 'linkedin.com/in/sushraju',
    'github' : 'github.com/sushraju',
    'twitter' : 'sushraju',
    'soundcloud': 'mediumcoffee',
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience,
    }

