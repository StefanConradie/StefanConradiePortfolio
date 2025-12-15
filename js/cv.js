// CV data and utilities

// Summary
const summaryData = "Results-driven Data Analyst with expertise in predictive and advanced analytics, data engineering, and cloud solutions. Skilled in Python, SQL, Azure Databricks, and AI-driven automation, with a proven record of transforming complex datasets into actionable insights across investment banking, telecommunications, healthcare, and renewable energy. Strong in stakeholder engagement, data governance, and business intelligence visualisation.";

// Contact Information
const contactData = {
  phone: "+44 744 277 1561",
  email: "stefan.alwyn.conradie@gmail.com",
  linkedin: "linkedin.com/in/stefan-conradie-link"
};

// Work Experience data
const workExperienceData = [
  {
    title: "Senior Analyst",
    company: "BDO LLP",
    location: "London, United Kingdom",
    startDate: "2023-01-01",
    endDate: null, // null means current position
    responsibilities: [
      "Led optimisation of an enterprise-scale data migration project and banking reconciliation system initiatives, leveraging big data technologies and ETL processes.",
      "Developed and deployed predictive analytics models and implemented interactive Power BI dashboards to support business performance monitoring.",
      "Performed in-depth system efficiency reviews and analytics to identify usage trends and optimisation opportunities across investment banking, telecommunications, and energy sectors.",
      "Designed and implemented robust data governance frameworks, ensuring compliance and data quality standards were maintained across projects.",
      "Managed senior stakeholder relationships and coordinated cross-functional teams to deliver complex technical solutions within project timelines.",
      "Built programmatic AI agents, including an automated complaints handling agent, to streamline workflows using Microsoft Copilot and API integrations, improving efficiency in complaint resolution and reporting."
    ]
  }
];

// Projects data
const projectsData = [
  {
    title: "AI-Powered Complaints Agent",
    technologies: "Microsoft Copilot, API Integration, Python",
    year: "2025",
    description: "Developed an automated complaints handling agent leveraging AI APIs and Microsoft Copilot to streamline user input processing, complaint resolution, and reporting. Built real-time dashboards and visualisations to track complaint resolution metrics, significantly reducing manual effort and improving client satisfaction."
  },
  {
    title: "Reconciliation Logic Review",
    technologies: "Financial Services, Data Governance, Risk & Compliance",
    year: "2025",
    description: "Assessed and validated reconciliation logic across legacy systems to ensure data completeness and regulatory compliance. Delivered recommendations that improved data reliability, reduced risk exposure, and enhanced strategic agility."
  },
  {
    title: "ESG Data Model Optimisation",
    technologies: "Waste Management, Data Governance, KPI Reporting",
    year: "2025",
    description: "Reviewed and optimised ESG data models to align with net-zero targets and evolving reporting frameworks. Improved data accuracy, reduced manual effort, and strengthened decision-making through a phased implementation roadmap."
  },
  {
    title: "Revenue Assurance & Billing Audit",
    technologies: "Telecommunications, Databricks, Power BI",
    year: "2024",
    description: "Reconciled 10M+ daily transactions to uncover £15.5M in potential revenue leakage and billing discrepancies. Enhanced billing transparency and operational efficiency through data-driven insights and governance recommendations."
  },
  {
    title: "HCM Data Migration",
    technologies: "Health, Azure Data Factory, Python, Workday",
    year: "2024",
    description: "Engineered scalable ADF pipelines and Python scripts to automate HCM data transformation and migration for 17K+ employees. Enabled a 2-day cutover and delivered £1.2M in project value while establishing reusable components for future initiatives."
  }
];

// Education data
const educationData = [
  {
    degree: "Applied Mathematics Honours Degree",
    institution: "Stellenbosch University",
    location: "Stellenbosch, South Africa",
    faculty: "Faculty of Applied Mathematics",
    startDate: "2022-01-01",
    endDate: "2022-12-31"
  },
  {
    degree: "Applied Mathematics Degree",
    institution: "Stellenbosch University",
    location: "Stellenbosch, South Africa",
    faculty: "Faculty of Applied Mathematics",
    startDate: "2019-01-01",
    endDate: "2021-12-31"
  }
];

// Skills data organized by category
const skillsData = {
  programming: [
    "Python (Pandas, NumPy, TensorFlow, Scikit-learn)",
    "R",
    "SQL",
    "HTML"
  ],
  tools: [
    "Azure Databricks",
    "Microsoft Copilot",
    "Git",
    "SSMS",
    "Power BI",
    "Power Platform",
    "Tableau"
  ],
  dataEngineering: [
    "ETL Processes",
    "Data Warehousing",
    "Database Management"
  ],
  analytics: [
    "Predictive Modelling",
    "Sentiment Analysis",
    "Text Extraction",
    "Time Series Analysis"
  ],
  aiAutomation: [
    "Programmatic AI Agents",
    "API Integration",
    "Agentic AI Automation"
  ],
  businessIntelligence: [
    "Advanced Data Visualisation",
    "Statistical Analysis",
    "Process Optimisation"
  ],
  projectManagement: [
    "Stakeholder Management",
    "Resource Planning",
    "Requirements Gathering"
  ]
};

// Certifications data
const certificationsData = [
  {
    name: "MySQL for Data Analytics and Business Intelligence",
    issuer: "Udemy",
    issueDate: "2022-01-01"
  },
  {
    name: "Azure Fundamentals (AZ-900)",
    issuer: "Microsoft",
    issueDate: "2023-02-01"
  },
  {
    name: "Security, Compliance, and Identity Fundamentals",
    issuer: "Microsoft",
    issueDate: "2023-08-01"
  },
  {
    name: "Microsoft 365 Fundamentals",
    issuer: "Microsoft",
    issueDate: "2023-08-01"
  },
  {
    name: "AQR License",
    issuer: "BDO UK",
    issueDate: "2024-04-01"
  }
];

export async function getSummary() {
  return summaryData;
}

export async function getContact() {
  return contactData;
}

export async function getWorkExperience() {
  return workExperienceData
    .sort((a, b) => {
      // Sort by endDate (null/current positions first, then by date descending)
      if (!a.endDate && !b.endDate) return 0;
      if (!a.endDate) return -1;
      if (!b.endDate) return 1;
      return new Date(b.endDate) - new Date(a.endDate);
    });
}

export async function getProjects() {
  return projectsData.sort((a, b) => parseInt(b.year) - parseInt(a.year));
}

export async function getEducation() {
  return educationData
    .sort((a, b) => new Date(b.endDate || b.startDate) - new Date(a.endDate || a.startDate));
}

export async function getSkills() {
  return skillsData;
}

export async function getCertifications() {
  return certificationsData.sort((a, b) => new Date(b.issueDate) - new Date(a.issueDate));
}
