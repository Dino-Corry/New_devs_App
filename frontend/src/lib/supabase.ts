import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.error('Missing Supabase environment variables:', {
    url: !!supabaseUrl,
    anonKey: !!supabaseAnonKey
  });
  throw new Error('Missing Supabase environment variables');
}

console.log('Creating Supabase client with URL:', supabaseUrl);

// Simple localStorage adapter - Supabase handles session management
// Profile isolation is not needed since each browser profile has separate localStorage
const createStorageAdapter = () => {
  console.log('[Supabase] Using localStorage for session persistence');
  return window.localStorage;
};

// Create Supabase client with anonymous key for frontend operations
export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    persistSession: true,
    autoRefreshToken: true,
    storage: createStorageAdapter(),
    storageKey: `sb-${supabaseUrl.split('//')[1].split('.')[0]}-auth-token`,
    detectSessionInUrl: true,
    flowType: 'pkce',
    debug: import.meta.env.DEV,
  },
  global: {
    headers: {
      'x-client-info': 'property-management-system'
    }
  },
  // LOCALHOST FIX: Ensure realtime works on localhost
  realtime: {
    params: {
      eventsPerSecond: 10
    }
  }
});

// LOCALHOST FIX: Force session check on page load
if (typeof window !== 'undefined') {
  supabase.auth.getSession().then(({ data: { session } }) => {
    if (session) {
      console.log('✅ Session found on page load:', session.user.email);
    } else {
      console.log('ℹ️ No session found on page load');
    }
  });
}

// For admin operations, use the FastAPI backend instead of direct admin client
export const adminClient = supabase; // Frontend uses same client, backend handles admin operations

export default supabase;