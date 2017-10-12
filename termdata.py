business_terms = {
    'Corporation': [
        'company', 'incorporated', 'corporation', 'corp.', 'corp', 'inc',
        '& co.', '& co', 'inc.', 's.p.a.', 'n.v.', 'a.g.', 'ag', 'nuf', 's.a.',
        's.f.', 'oao', 'co.', 'co'
    ],
    'General Partnership': [
        'soc.col.', 'stg', 'd.n.o.', 'ltda.', 'v.o.s.', 'a spol.',
        u've\xc5\x99. obch. spol.', 'kgaa', 'o.e.', 's.f.', 's.n.c.',
        's.a.p.a.', 'j.t.d.', 'v.o.f.', 'sp.j.', 'og', 'sd', ' i/s', 'ay',
        'snc', 'oe', 'bt.', 's.s.', 'mb', 'ans', 'da', 'o.d.', 'hb', 'pt'
    ],
    'Joint Stock / Unlimited': [
        'unltd', 'ultd', 'sal', 'unlimited', 'saog', 'saoc', 'aj', 'yoaj',
        'oaj', 'akc. spol.', 'a.s.'
    ],
    'Joint Venture': ['esv', 'gie', 'kv.', 'qk'],
    'Limited': [
        'pty. ltd.', 'pty ltd', 'ltd', 'l.t.d.', 'bvba', 'd.o.o.', 'ltda',
        'gmbh', 'g.m.b.h', 'kft.', 'kht.', 'zrt.', 'ehf.', 's.a.r.l.',
        'd.o.o.e.l.', 's. de r.l.', 'b.v.', 'tapui', 'sp. z.o.o.', 's.r.l.',
        's.l.', 's.l.n.e.', 'ood', 'oy', 'rt.', 'teo', 'uab', 'scs', 'sprl',
        'limited', 'bhd.', 'sdn. bhd.', 'sdn bhd', 'as', 'lda.', 'tov', 'pp'
    ],
    'Limited Liability Company': [
        'pllc', 'llc', 'l.l.c.', 'plc.', 'plc', 'hf.', 'oyj', 'a.e.', 'nyrt.',
        'p.l.c.', 'sh.a.', 's.a.', 's.r.l.', 'srl.', 'aat', '3at', 'd.d.',
        's.r.o.', 'spol. s r.o.', 's.m.b.a.', 'smba', 'sarl', 'nv', 'sa',
        'aps', 'a/s', 'p/s', 'sae', 'sasu', 'eurl', 'ae', 'cpt', 'as', 'ab',
        'asa', 'ooo', 'dat', 'vat', 'zat', 'mchj', 'a.d.'
    ],
    'Limited Liability Limited Partnership': ['lllp', 'l.l.l.p.'],
    'Limited Liability Partnership':
    ['llp', 'l.l.p.', 'sp.p.', 's.c.a.', 's.c.s.'],
    'Limited Partnership': [
        'gmbh & co. kg', 'gmbh & co. kg', 'lp', 'l.p.', 's.c.s.', 's.c.p.a',
        'comm.v', 'k.d.', 'k.d.a.', 's. en c.', 'e.e.', 's.a.s.', 's. en c.',
        'c.v.', 's.k.a.', 'sp.k.', 's.cra.', 'ky', 'scs', 'kg', 'kd', 'k/s',
        'ee', 'secs', 'kda', 'ks', 'kb', 'kt'
    ],
    'Mutual Fund': ['sicav'],
    'No Liability': ['nl'],
    'Non-Profit': ['vzw', 'ses.', 'gte.'],
    'Private Company': ['private', 'pte', 'xk'],
    'Professional Association': ['p.a.', 'pa'],
    'Professional Corporation': ['p.c.', 'vof', 'snc', 'pc'],
    'Professional Limited Liability Company': ['pllc', 'p.l.l.c.', 'pl', 'p.l.'],
    'Sole Proprietorship': [
        'e.u.', 's.p.', 't:mi', 'tmi', 'e.v.', 'e.c.', 'et', 'obrt', 'fie',
        'ij', 'fop', 'xt'
    ],
}

medical_terms = {
    'Doctor of Dental Surgery': ['d.d.s.', 'd.d.o.', 'dds', 'ddo'],
    'Doctor of Medical Dentistry': ['d.m.d.', 'dmd'],
    'Doctor of Osteopathy': ['d.o.', 'do'],
    'Doctor of Podiatric Medicine': ['d.p.m.', 'dpm'],
    'Doctor of Medicine': ['dr.', 'dr', 'doctor of medicine'],
    'Fellow of the American Academy of Dermatology': ['f.a.a.d.', 'faad'],
    'Fellow of the American Academy of Emergency Medicine':
    ['f.a.a.e.m.', 'faaaem'],
    'Fellow of the American Academy of Family Physicians':
    ['f.a.a.f.p.', 'faafp'],
    'Fellow of the American College of Cardiologists': ['f.a.c.c.', 'facc'],
    'Fellow of the American College of Endocrinology': ['f.a.c.e.'],
    'Fellow of the American College of Emergency Physicians':
    ['f.a.c.e.p.', 'facep'],
    'Fellow of the American College of Gastroenterology': ['f.a.c.g.', 'facg'],
    'Fellow of the American College of Foot and Ankle Surgeons': [
        'f.a.c.f.a.s.', 'facfas'
    ],
    'Fellow of the American College of Obstetrics and Gynecologists': [
        'f.a.c.o.g.', 'facog'
    ],
    'Fellow of the American College of Osteopathic Surgeons': [
        'f.a.c.o.s.', 'facos'
    ],
    'Fellow of the American College of Physicians': ['f.a.c.p.', 'facp'],
    'Fellow of the American College of Chest Physicians': [
        'f.a.c.c.p.', 'faccp'
    ],
    'Fellow of the American College of Surgeons': ['f.a.c.s.', 'facs'],
    'Fellow of the American Society of Podiatric Surgeons': [
        'f.a.s.p.s.', 'fasps'
    ],
    'Fellow in Hospital Medicine': ['f.h.m.', 'fhm'],
    'Fellow of the International College of Surgeons': ['f.i.c.s.', 'fics'],
    'Fellow of the Society for Cardiovascular Angiography and Interventions': [
        'f.s.c.a.i.', 'fscai'
    ],
    'Fellow of the Society of Thoracic Surgeons': ['f.s.t.s.', 'fsts'],
    'Medical Doctor': ['m.d.', 'md'],
    'Master of Public Health': ['m.p.h.'],
    'Nurse Practitioner': [
        'n.p.', 'np', 'a.r.n.p', 'arnp', 'a.c.n.p', 'acnp', 'a.g.n.p', 'agnp',
        'c.f.n.p', 'cfnp'
    ],
    'Doctor of Optometry': ['o.d.', 'od'],
    'Orthodontist': ['orthdont'],
    'Physician Assistant': ['p.a.'],
    'Doctor of Philosophy': ['dphil', 'ph.d.', 'phd', 'ph d'],
    'Registered Nurse': [
        'r.n.', 'rn', 'a.p.r.n.', 'aprn', 'rn cnp', 'rn, cnp', 'rncp'
    ],
    'Doctor of Psychology': ['psyd', 'psy.d', 'psych'],
    'Medical Student Life Advisory Committee': ['mslac', 'ms, lac'],
    'Women'
    's Health Care Nurse Practitioner': ['whcnp', 'whnp'],
    'Certified Nurse Midwife': ['c.n.m.', 'cnm'],
    'Doctor of Audiology': ['a.u.d.', 'aud'],
    'Doctor of Chiropractic': ['d.c.', 'dc'],
    'Doctor of Physical Therapy': ['d.p.t.', 'dpt'],
    'Doctor of Science in Physical Therapy': ['d.s.c.p.t.', 'dscpt'],
    'Doctor of Science in Nursing': ['d.s.n.', 'dsn'],
    'Doctor of Veterinary Medicine': ['d.v.m.', 'dvm'],
    'Ear, Nose and Throat Specialist': ['e.n.t.', 'ent'],
    'General Practitioner': ['g.p.', 'gp'],
    'Gynecologist': ['gyn'],
    'Master of Surgery': ['ms'],
    'Obstetrician and Gynecologist': ['ob/gyn', 'obgyn', 'ob gyn'],
    'Doctor of Pharmacy': ['pharmd', 'pharm.d'],
    'Fellow Faculty of Radiologists': ['ffr'],
    'Fellow of the Royal College of Physicians and Surgeons of Canada': [
        'frcpsc'
    ],
    'Member Royal College of Obstetricians and Gynecologists': ['mrcog'],
    'Member Royal College of Surgeons': ['mrcs'],
    'Doctor of Divinity': ['dd'],
    'Doctor of Education': ['ded', 'edd'],
    'Doctor of Public Administration': ['dpa'],
    'Doctor of Public Health': ['dph'],
    'Fellow Faculty of Public Health Medicine': ['ffphm'],
    'Doctor of Jurisprudence': ['jd'],
    'Doctor of Science': ['scd'],
    'Doctor of Social Science': ['sscd'],
    'Doctor of Theology': ['thd'],
    'Certificate of Clinical Competence': ['ccc'],
    'Fellow of the American College of Obstetricians and Gynecologists': [
        'facog'
    ],
    'Family Nurse Practitioner': ['fncp'],
    'Licensed Clinical Professional Counselor': ['lcpc', 'lpc'],
    'Licensed Marriage and Family Therapist': ['lmft'],
    'Marriage, Family and Child Counselor': ['mfcc'],
    'Marriage and Family Therapists': ['mft'],
    'Licensed Mental Health Counselor': ['lmhc', 'lcmhc', 'cmhc'],
    'Licensed Mental Health Professional': ['lmhp'],
    'Licensed Professional Clinical Counselor': ['lpcc'],
    'Bachelor of Medicine': [
        'mbbs', 'mbchb', 'mbbch', 'mb bchir', 'bm bch', 'bmbs'
    ],
    'Occupational Therapist': ['otr', 'otrl', 'otr/l', 'otr l'],
    'Psychiatric-Mental Health Nurse Practitioner': ['pmhnp'],
    'Pediatric Nurse Practitioner': ['pnp'],
}

lawyer_terms = {
    'Juris Doctor': ['j.d.', 'jd'],
    'Bachelor of Laws': ['ll.b', 'llb', 'l.l.b.'],
    'Master of Laws': ['ll.m', 'llm', 'l.l.m.'],
    'Doctor of Juridical Studies': ['jsd', 'j.s.d.', 'sjd', 's.j.d.'],
    'Esquire': ['esq', 'esq.'],
    'Attorney': ['atty', 'attorney'],
    'Lawyer': ['lwyr', 'lawyer'],
}

real_estate_terms = {
    'Accredited Buyer Representative': ['abr'],
    'Accredited Management Organization': ['amo'],
    'Certified Buyer Representative': ['cbr'],
    'Certified Home Marketing Specialist': ['chms'],
    'Certified Luxury Home Marketing Specialist': ['clhms'],
    'Certified Negotiation Specialist': ['cns'],
    'Certified Property Manager': ['cpm'],
    'Certified Real Estate Broker': ['crb'],
    'Certified Residential Specialist': ['crs'],
    'Graduate Realtor Institute': ['gri'],
    'Graduate Real Estate Society': ['gres'],
    'Graduate REALTOR® Institute': ['gri'],
    'National Association of Realtors': ['nar'],
    'Member of the National Association of Realtors': ['realtor'],
    'Real Estate Board of New York': ['rebny'],
    'Realtors Political Action Committee': ['rpac'],
    'Senior Real Estate Specialist': ['sres'],
}

insurance_terms = {
    'Certified Insurance Counselor': ['cic'],
    'Certified Risk Manager': ['crm'],
    'Associate in Risk Management': ['arm'],
    'Associate In General Insurance': ['ains'],
    'Accredited Advisor in Insurance': ['aai'],
    'Personal Lines Coverage Specialist': ['plcs'],
    'Certified Insurance Service Representative': ['cisr'],
    'Associate in Insurance Services': ['ais'],
    'Associate in Claims': ['aic'],
    'Chartered Life Underwriter': ['clu'],
    'Life Underwriter Training Council Fellow': ['lutcf'],
    'Financial Services Certified Professional': ['fscp'],
    'Certified Financial Planner': ['cfp'],
    'Registered Health Underwriter': ['rhu'],
    'Professional, Health Insurance Advanced Studies': ['fhias'],
    'Professional, Academy for Healthcare Management': ['pahm'],
    'Chartered Healthcare Consultant': ['chhc'],
    'Healthcare Customer Service Associate': ['hcsa'],
    'Health Insurance Associate': ['hia'],
    'Healthcare Compliance Professional': ['hcp'],
    'Fellow, Life and Health Claims': ['flhc'],
    'Group Benefits Associate': ['gba'],
    'Managed Healthcare Professional': ['mhp'],
    'Chartered Property Casualty Underwriter': ['cpcu'],
    'Commercial Lines Coverage Specialist': ['clcs']
}

other_terms = {
    'Certified Public Accountant': ['c.p.a', 'cpa'],
    'Academy of Certified Social Workers': ['a.c.s.w.', 'acsw'],
    'Licensed Clinical Social Worker':
    ['lcsw', 'lcsw-c', 'lcswc', 'lcsw-r', 'lcswr', 'lcswacsw'],
    'Licensed Independent Social Worker': ['lisw'],
    'Master of Social Work': ['msw', 'mssw', 'msa'],
    'Service': ['service', 'svc'],
}

terms_by_type = {**business_terms, **medical_terms, **lawyer_terms,
                 **real_estate_terms, **insurance_terms, **other_terms}

terms_by_country = {
    'Albania': ['sh.a.', 'sh.p.k.'],
    'Argentina': [
        's.a.', 's.r.l.', 's.c.p.a', 'scpa', 's.c.e i.', 's.e.', 's.g.r',
        'soc.col.'
    ],
    'Australia': ['nl', 'pty. ltd.', 'pty ltd'],
    'Austria': ['e.u.', 'stg', 'gesbr', 'a.g.', 'ag', 'og', 'kg'],
    'Belarus': ['aat', '3at'],
    'Belgium': [
        'esv', 'vzw', 'vof', 'snc', 'comm.v', 'scs', 'bvba', 'sprl', 'cbva',
        'cvoa', 'sca', 'sep', 'gie'
    ],
    'Bosnia / Herzegovina':
    ['d.d.', 'a.d.', 'd.n.o.', 'd.o.o.', 'k.v.', 's.p.'],
    'Brazil':
    ['ltda', 's.a.', 'pllc', 'ad', 'adsitz', 'ead', 'et', 'kd', 'kda', 'sd'],
    'Bulgaria': ['ad', 'adsitz', 'ead', 'et', 'kd', 'kda', 'sd'],
    'Cambodia': ['gp', 'sm pte ltd.', 'pte ltd.', 'plc ltd.', 'peec', 'sp'],
    'Canada': ['gp', 'lp', 'sp'],
    'Chile': [
        'eirl', 's.a.', 'sgr', 's.g.r.', 'ltda', 's.p.a.', 'sa', 's. en c.',
        'ltda.'
    ],
    'Columbia': ['s.a.', 'e.u.', 's.a.s.', 'suc. de descendants', 'sca'],
    'Croatia': ['d.d.', 'd.d.o.', 'obrt'],
    'Czech Republic': [
        'a.s.', 'akc. spol.', 's.r.o.', 'spol. s r.o.', 'v.o.s.',
        u've\xc5\x99. obch. spol.', 'a spol.', 'k.s.', 'kom. spol.',
        'kom. spol.'
    ],
    'Denmark': [
        'i/s', 'a/s', 'k/s', 'p/s', 'amba', 'a.m.b.a.', 'fmba', 'f.m.b.a.',
        'smba', 's.m.b.a.', 'g/s'
    ],
    'Dominican Republic':
    ['c. por a.', 'cxa', 's.a.', 's.a.s.', 'srl.', 'eirl.', 'sa', 'sas'],
    'Ecuador': ['s.a.', 'c.a.', 'sa', 'ep'],
    'Egypt': ['sae'],
    'Estonia': ['fie'],
    'Finland': [
        't:mi', 'tmi', 'as oy', 'as.oy', 'ay', 'ky', 'oy', 'oyj', 'ok'
    ],
    'France': [
        'sicav', 'sarl', 'sogepa', 'ei', 'eurl', 'sasu', 'fcp', 'gie', 'sep',
        'snc', 'scs', 'sca', 'scop', 'sem', 'sas'
    ],
    'Germany': [
        'gmbh & co. kg', 'gmbh & co. kg', 'e.g.', 'e.v.', 'gbr', 'ohg',
        'partg', 'kgaa', 'gmbh', 'g.m.b.h.', 'ag'
    ],
    'Greece': [
        'a.e.', 'ae', 'e.e.', 'ee', 'epe', 'e.p.e.', 'mepe', 'm.e.p.e.',
        'o.e.', 'oe', 'ovee', 'o.v.e.e.'
    ],
    'Guatemala': ['s.a.', 'sa'],
    'Haiti': ['sa'],
    'Hong Kong': ['ltd', 'unltd', 'ultd', 'limited'],
    'Hungary': [
        'e.v.', 'e.c.', 'bt.', 'kft.', 'kht.', 'kkt.', 'k.v.', 'zrt.', 'nyrt',
        'ev', 'ec', 'rt.'
    ],
    'Iceland': ['ehf.', 'hf.', 'ohf.', 's.f.', 'ses.'],
    'India': ['pvt. ltd.', 'ltd.', 'psu', 'pse'],
    'Indonesia': ['ud', 'fa', 'pt'],
    'Ireland': ['cpt', 'teo'],
    'Israel': ['b.m.', 'bm', 'ltd', 'limited'],
    'Italy': [
        's.n.c.', 's.a.s.', 's.p.a.', 's.a.p.a.', 's.r.l.', 's.c.r.l.', 's.s.'
    ],
    'Latvia': ['as', 'sia', 'ik', 'ps', 'ks'],
    'Lebanon': ['sal'],
    'Lithuania': ['uab', 'ab', 'ij', 'mb'],
    'Luxemborg': ['s.a.', 's.a.r.l.', 'secs'],
    'Macedonia': ['d.o.o.', 'd.o.o.e.l', 'k.d.a.', 'j.t.d.', 'a.d.', 'k.d.'],
    'Malaysia': ['bhd.', 'sdn. bhd.'],
    'Mexico': ['s.a.', 's. de. r.l.', 's. en c.', 's.a.b.', 's.a.p.i.'],
    'Mongolia': ['xk', 'xxk'],
    'Netherlands': ['v.o.f.', 'c.v.', 'b.v.', 'n.v.'],
    'New Zealand': ['tapui', 'ltd', 'limited'],
    'Nigeria': ['gte.', 'plc', 'ltd.', 'ultd.'],
    'Norway': [
        'asa', 'as', 'ans', 'ba', 'bl', 'da', 'etat', 'fkf', 'hf', 'iks', 'kf',
        'ks', 'nuf', 'rhf', 'sf'
    ],
    'Oman': ['saog', 'saoc'],
    'Pakistan': ['ltd.', 'pvt. ltd.', 'ltd', 'limited'],
    'Peru': ['sa', 's.a.', 's.a.a.'],
    'Philippines':
    ['coop.', 'corp.', 'corp', 'ent.', 'inc.', 'inc', 'llc', 'l.l.c.', 'ltd.'],
    'Poland': [
        'p.p.', 's.k.a.', 'sp.j.', 'sp.k.', 'sp.p.', 'sp. z.o.o.', 's.c.',
        's.a.'
    ],
    'Portugal': ['lda.', 'crl', 's.a.', 's.f.', 'sgps'],
    'Romania': ['s.c.a.', 's.c.s.', 's.n.c.', 's.r.l.', 'o.n.g.', 's.a.'],
    'Russia': ['ooo', 'oao', 'zao', '3ao'],
    'Serbia': ['d.o.o.', 'a.d.', 'k.d.', 'o.d.'],
    'Singapore': ['bhd', 'pte ltd', 'sdn bhd', 'llp', 'l.l.p.', 'ltd.', 'pte'],
    'Slovenia': ['d.d.', 'd.o.o.', 'd.n.o.', 'k.d.', 's.p.'],
    'Slovakia': [
        'a.s.', 'akc. spol.', 's.r.o.', 'spol. s r.o.', 'k.s.', 'kom. spol.',
        'v.o.s.', 'a spol.'
    ],
    'Spain': [
        's.a.', 's.a.d.', 's.l.', 's.l.l.', 's.l.n.e.', 's.c.', 's.cra',
        's.coop', 'sal', 'sccl'
    ],
    'Sweden': ['ab', 'hb', 'kb'],
    'Switzerland': ['ab', 'sa', 'gmbh', 'g.m.b.h.', 'sarl', 'sagl'],
    'Turkey': ['koop.'],
    'Ukraine': [
        'dat', 'fop', 'kt', 'pt', 'tdv', 'tov', 'pp', 'vat', 'zat', 'at'
    ],
    'United Kingdom': [
        'plc.', 'plc', 'cic', 'cio', 'l.l.p.', 'llp', 'l.p.', 'lp', 'ltd.',
        'ltd', 'limited'
    ],
    'United States of America': [
        'llc', 'inc.', 'corporation', 'incorporated', 'company', 'limited',
        'corp.', 'inc.', 'inc', 'llp', 'l.l.p.', 'pllc', 'and company',
        '& company', 'inc', 'inc.', 'corp.', 'corp', 'ltd.', 'ltd', '& co.',
        '& co', 'co.', 'co', 'lp'
    ],
    'Uzbekistan': [
        'mchj', 'qmj', 'aj', 'oaj', 'yoaj', 'xk', 'xt', 'ok', 'uk', 'qk'
    ]
}
